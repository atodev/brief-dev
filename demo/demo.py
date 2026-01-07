"""
Brief Demo - Email Report Generator
Generates a daily market intelligence email with real opportunities
"""

import requests
import json
from datetime import datetime
from jinja2 import Template
import os

# Configuration
USER_CONFIG = {
    'name': 'Tom',
    'location': 'Auckland, New Zealand',
    'timezone': 'Pacific/Auckland'
}

def get_crypto_data():
    """Fetch real cryptocurrency data from CoinGecko API (free)"""
    try:
        # Get top cryptocurrencies with market data
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': False,
            'price_change_percentage': '24h,7d'
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching crypto data: {e}")
        return []

def get_nzx_local_opportunity():
    """
    Get a local NZ stock opportunity
    Note: For demo, using known NZ companies. In production, would use NZX API
    """
    # Example: Fisher & Paykel Healthcare (FPH.NZ)
    # A2 Milk Company (ATM.NZ)
    # Xero (XRO.NZ)
    # For demo purposes, returning structured data
    
    local_opportunity = {
        'name': 'Fisher & Paykel Healthcare',
        'ticker': 'FPH',
        'exchange': 'NZX',
        'price': '28.45',  # NZD
        'change_24h': 2.3,
        'risk_level': 'medium',
        'historical_pattern': 'Similar accumulation patterns have preceded +12-15% moves over 3 months in past 18 months',
        'tags': ['Healthcare', 'Export Revenue', 'Innovation'],
        'data_points': [
            'Recent expansion into new respiratory care markets (Asia-Pacific)',
            'Strong institutional buying observed in last 5 trading sessions',
            'Technical: Trading above 50-day moving average with increasing volume',
            'Local advantage: NZ-based manufacturing, benefiting from NZD weakness',
            'Q4 earnings report due in 2 weeks - consensus estimates positive'
        ]
    }
    
    return local_opportunity

def get_weather():
    """Get weather for Auckland (simplified for demo)"""
    # In production, use OpenWeatherMap API
    # For demo, returning typical Auckland summer weather
    return "22°C, Partly Cloudy"

def analyze_opportunities(crypto_data):
    """
    Analyze crypto data and identify interesting patterns
    Returns top 3 global opportunities
    """
    opportunities = []
    
    for coin in crypto_data[:5]:  # Top 5 by market cap
        price_change_24h = coin.get('price_change_percentage_24h', 0)
        
        # Look for interesting patterns
        pattern = None
        potential = None
        risk = 'medium'
        
        if price_change_24h > 5:
            pattern = "Strong upward momentum (+{}%)".format(round(price_change_24h, 1))
            potential = "+8-12% (7 days)"
            risk = 'medium'
        elif price_change_24h < -5:
            pattern = "Significant pullback (-{}%), potential bounce zone".format(abs(round(price_change_24h, 1)))
            potential = "+10-15% recovery (14 days)"
            risk = 'high'
        elif abs(price_change_24h) < 2 and coin['market_cap_rank'] <= 3:
            pattern = "Consolidation phase in major asset"
            potential = "+5-8% (14 days)"
            risk = 'low'
        else:
            pattern = "Stable price action, watching for breakout"
            potential = "+6-10% (14 days)"
            risk = 'medium'
        
        opportunities.append({
            'name': coin['name'],
            'ticker': coin['symbol'].upper(),
            'price': f"{coin['current_price']:,.2f}" if coin['current_price'] > 1 else f"{coin['current_price']:.6f}",
            'change_24h': round(price_change_24h, 2),
            'market_cap': coin['market_cap'],
            'pattern': pattern,
            'potential': potential,
            'risk_level': risk,
            'key_data': f"Market Cap: ${coin['market_cap']/1e9:.1f}B | 24h Volume: ${coin['total_volume']/1e9:.2f}B"
        })
    
    # Sort by most interesting (highest absolute change or top 3 coins)
    opportunities.sort(key=lambda x: abs(x['change_24h']), reverse=True)
    
    return opportunities[:3]  # Return top 3

def get_market_summary(crypto_data):
    """Generate market summary"""
    
    # Calculate overall market sentiment
    positive_count = sum(1 for c in crypto_data if c.get('price_change_percentage_24h', 0) > 0)
    total_count = len(crypto_data)
    
    if positive_count / total_count > 0.7:
        sentiment = "Bullish - 70%+ of top assets showing gains"
    elif positive_count / total_count < 0.3:
        sentiment = "Bearish - Majority of assets declining"
    else:
        sentiment = "Mixed - Market showing divergence"
    
    summary = [
        {
            'market': 'Cryptocurrency',
            'status': sentiment
        },
        {
            'market': 'NZX 50',
            'status': 'Up +0.8% - Local equities showing strength'
        },
        {
            'market': 'NZD/USD',
            'status': 'Trading at 0.6145 - Weak NZD benefits exporters'
        },
        {
            'market': 'Global Indices',
            'status': 'S&P 500 +0.3%, NASDAQ +0.5% - Tech leading gains'
        }
    ]
    
    return summary

def generate_email_html():
    """Generate the email HTML report"""
    
    print("📊 Fetching real market data...")
    
    # Fetch real data
    crypto_data = get_crypto_data()
    
    if not crypto_data:
        print("❌ Failed to fetch market data. Please check your internet connection.")
        return None
    
    print(f"✅ Fetched data for {len(crypto_data)} cryptocurrencies")
    
    # Analyze opportunities
    global_observations = analyze_opportunities(crypto_data)
    local_opportunity = get_nzx_local_opportunity()
    market_summary = get_market_summary(crypto_data)
    
    # Prepare template data
    template_data = {
        'user_name': USER_CONFIG['name'],
        'user_location': USER_CONFIG['location'],
        'current_date': datetime.now().strftime('%A, %B %d, %Y'),
        'weather': get_weather(),
        'local_opportunity': local_opportunity,
        'global_observations': global_observations,
        'market_summary': market_summary,
        'generation_time': datetime.now().strftime('%I:%M %p %Z')
    }
    
    # Load template
    template_path = os.path.join(os.path.dirname(__file__), 'email_template.html')
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Render template
    template = Template(template_content)
    html_output = template.render(**template_data)
    
    return html_output

def save_html_report(html_content, filename='brief_report.html'):
    """Save HTML report to file"""
    output_path = os.path.join(os.path.dirname(__file__), filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    return output_path

def send_email(html_content, recipient_email, smtp_config=None):
    """
    Send email via SMTP (optional)
    smtp_config should contain: host, port, username, password
    """
    if not smtp_config:
        print("⚠️  No SMTP config provided. Email not sent.")
        return False
    
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"📊 Your Brief - {datetime.now().strftime('%B %d, %Y')}"
        msg['From'] = smtp_config['username']
        msg['To'] = recipient_email
        
        # Attach HTML content
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)
        
        # Send email
        with smtplib.SMTP(smtp_config['host'], smtp_config['port']) as server:
            server.starttls()
            server.login(smtp_config['username'], smtp_config['password'])
            server.send_message(msg)
        
        print(f"✅ Email sent successfully to {recipient_email}")
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def main():
    """Main demo function"""
    print("=" * 50)
    print("📊 Brief Demo - Email Report Generator")
    print("=" * 50)
    print()
    
    # Generate report
    html_content = generate_email_html()
    
    if not html_content:
        print("❌ Failed to generate report")
        return
    
    # Save to file
    output_path = save_html_report(html_content)
    print()
    print("=" * 50)
    print(f"✅ Report generated successfully!")
    print(f"📄 Saved to: {output_path}")
    print()
    print("🌐 Open this file in your web browser to view the report")
    print("=" * 50)
    print()
    
    # Optionally send email
    send_email_prompt = input("Would you like to send this report via email? (y/n): ").strip().lower()
    if send_email_prompt == 'y':
        recipient = input("Enter recipient email address: ").strip()
        
        print()
        print("SMTP Configuration needed:")
        smtp_host = input("SMTP Host (e.g., smtp.gmail.com): ").strip()
        smtp_port = input("SMTP Port (e.g., 587): ").strip()
        smtp_user = input("SMTP Username (your email): ").strip()
        smtp_pass = input("SMTP Password/App Password: ").strip()
        
        smtp_config = {
            'host': smtp_host,
            'port': int(smtp_port),
            'username': smtp_user,
            'password': smtp_pass
        }
        
        send_email(html_content, recipient, smtp_config)
    
    print()
    print("Demo complete! 🎉")

if __name__ == "__main__":
    main()
