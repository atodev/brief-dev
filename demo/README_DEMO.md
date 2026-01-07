# Brief Demo - Email Report Generator

## Overview

This is a **scaled-down demo** of Brief that generates a daily market intelligence email report with **real market opportunities**.

The demo fetches live data from financial APIs and generates a professional HTML email containing:

- 1 local opportunity (New Zealand stock)
- 3 global observations (cryptocurrency markets)
- Market summary
- Risk levels and potential outlined

## Features

✅ **Real Data**: Fetches live cryptocurrency prices from CoinGecko API (free, no API key needed)  
✅ **Local Focus**: Includes NZ-based stock opportunity (Fisher & Paykel Healthcare example)  
✅ **Risk Analysis**: Each opportunity shows risk level (Low/Medium/High) and potential gains  
✅ **Professional Design**: Beautiful HTML email template with responsive design  
✅ **Compliance**: All language framed as "observations" not "advice"  
✅ **No Database**: Simple Python script, no database setup required

## Quick Start

### 1. Install Python Dependencies

```bash
cd demo
pip install -r requirements.txt
```

### 2. Run the Demo

```bash
python demo.py
```

### 3. View the Report

The script will:

1. Fetch real market data from CoinGecko
2. Analyze patterns and identify opportunities
3. Generate an HTML email report
4. Save it as `brief_report.html`
5. Optionally send via email (SMTP)

**Open `brief_report.html` in your web browser to see the report!**

## What You'll See

### 📍 Local Opportunity (Auckland, NZ)

- **Fisher & Paykel Healthcare (FPH.NZ)**
- Real-time price and 24h change
- Risk level assessment
- Historical pattern analysis
- Key data points (earnings, institutional buying, technical indicators)

### 🌍 Global Observations

- **3 cryptocurrency opportunities** (Bitcoin, Ethereum, etc.)
- Real-time prices from CoinGecko API
- Pattern recognition (momentum, pullback, consolidation)
- Potential gain estimates
- Risk levels

### 📊 Market Summary

- Overall crypto market sentiment
- NZX 50 status
- NZD/USD forex rate
- Global indices (S&P 500, NASDAQ)

## Sample Output

```
==================================================
📊 Brief Demo - Email Report Generator
==================================================

📊 Fetching real market data...
✅ Fetched data for 10 cryptocurrencies

==================================================
✅ Report generated successfully!
📄 Saved to: G:\Fin-Advisor\demo\brief_report.html

🌐 Open this file in your web browser to view the report
==================================================
```

## Configuration

Edit `demo.py` to customize:

```python
USER_CONFIG = {
    'name': 'Tom',  # Your name
    'location': 'Auckland, New Zealand',  # Your location
    'timezone': 'Pacific/Auckland'
}
```

## Sending Email (Optional)

The demo can send the report via email using SMTP:

1. Run the demo: `python demo.py`
2. When prompted, choose `y` to send email
3. Enter recipient email address
4. Provide SMTP credentials:
   - **Gmail**: Use `smtp.gmail.com` port `587` with App Password
   - **Outlook**: Use `smtp.office365.com` port `587`
   - **Other**: Check your email provider's SMTP settings

### Gmail Setup (Recommended for Testing)

1. Go to Google Account → Security
2. Enable 2-Factor Authentication
3. Generate "App Password" for Mail
4. Use this password in the demo (not your regular Gmail password)

## API Usage

### CoinGecko API (Free Tier)

- **Rate Limit**: 10-50 calls/minute
- **No API Key**: Not required for basic usage
- **Data**: Real-time cryptocurrency prices, market cap, volume
- **Endpoint**: `https://api.coingecko.com/api/v3/coins/markets`

If you get rate-limited, wait 1 minute and try again.

## File Structure

```
demo/
├── demo.py                 # Main Python script
├── email_template.html     # Jinja2 HTML email template
├── requirements.txt        # Python dependencies
├── README_DEMO.md         # This file
└── brief_report.html      # Generated output (created after running)
```

## Demo Limitations

This is a simplified demo. Full Brief will include:

**Not Included in Demo**:

- ❌ Voice briefing
- ❌ Mobile app
- ❌ Portfolio tracking
- ❌ Community features
- ❌ Satellite imagery analysis
- ❌ User authentication
- ❌ Database storage
- ❌ Broker integrations

**Included in Demo**:

- ✅ Email report generation
- ✅ Real market data
- ✅ Opportunity identification
- ✅ Risk assessment
- ✅ Professional HTML design
- ✅ Compliance-friendly language

## Extending the Demo

### Add More Data Sources

**Stocks (US)**:

```python
# Add Yahoo Finance or Alpha Vantage API
import yfinance as yf
tesla = yf.Ticker("TSLA")
price = tesla.info['currentPrice']
```

**Forex**:

```python
# Add OANDA or Alpha Vantage
url = "https://api.exchangerate-api.com/v4/latest/NZD"
response = requests.get(url)
nzd_usd = response.json()['rates']['USD']
```

**News**:

```python
# Add NewsAPI
url = "https://newsapi.org/v2/everything"
params = {'q': 'Tesla', 'apiKey': 'YOUR_KEY'}
response = requests.get(url, params=params)
```

### Personalize Opportunities

```python
# Add user risk profile
USER_CONFIG = {
    'name': 'Tom',
    'location': 'Auckland, New Zealand',
    'risk_tolerance': 'moderate',  # conservative, moderate, aggressive
    'preferred_assets': ['stocks', 'crypto'],  # stocks, crypto, forex, commodities
    'investment_amount': 1000  # USD
}

# Filter opportunities by risk
if USER_CONFIG['risk_tolerance'] == 'conservative':
    opportunities = [o for o in opportunities if o['risk_level'] == 'low']
```

### Schedule Daily Reports

**Windows (Task Scheduler)**:

1. Open Task Scheduler
2. Create Basic Task
3. Trigger: Daily at 6:00 AM
4. Action: Start Program → `python.exe G:\Fin-Advisor\demo\demo.py`

**Linux/Mac (Cron)**:

```bash
# Edit crontab
crontab -e

# Add line (runs daily at 6 AM)
0 6 * * * cd /path/to/demo && python demo.py
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"

```bash
pip install -r requirements.txt
```

### "Failed to fetch market data"

- Check internet connection
- CoinGecko API may be rate-limited (wait 1 minute)
- Try again with `python demo.py`

### "Email sending failed"

- Verify SMTP credentials
- Gmail users: Use App Password, not regular password
- Check firewall/antivirus blocking port 587

### "HTML looks broken in browser"

- Some email clients strip CSS
- For best results, open in Chrome/Firefox
- Or send as email to view in Gmail/Outlook

## Next Steps

After testing the demo:

1. **Gather Feedback**: Show to potential users, collect reactions
2. **Expand Data Sources**: Add stocks, forex, commodities APIs
3. **Build MVP**: Web app with user accounts, portfolio tracking
4. **Add Features**: Voice briefing, mobile app, community
5. **Scale Infrastructure**: Move to cloud (AWS/Azure)

## Cost Estimate (Demo)

**Free Tier**:

- CoinGecko API: Free (10-50 calls/min)
- Python: Free
- HTML generation: Free
- Email sending: Free (use Gmail SMTP)

**Total Demo Cost**: $0

## Production Cost Estimate

For full Brief app (10,000 users):

- Alternative data APIs: $56K/month
- Cloud infrastructure: $2-9K/month
- Development team: $50K/month (5 engineers)
- **Total**: $108-115K/month

## Questions?

For questions or feedback:

- Email: [your-email]
- GitHub: https://github.com/atodev/brief-dev

---

**Disclaimer**: This demo provides market observations and educational content, not financial advice. All investment decisions are yours alone. Invest at your own risk.
