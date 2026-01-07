# Email Report Specification

## Overview

Each morning, users receive a comprehensive email report containing all the day's investment opportunities, detailed analysis, and supporting evidence. The email complements the voice briefing and serves as a reference document.

---

## Email Structure

### Subject Line (Personalized & Dynamic)

**Format**: `{Greeting} {Name} - Your Brief for {Date} | {Highlight}`

**Examples**:

- `Good Morning Alex - Your Brief for Jan 7 | 10 Opportunities Found`
- `Morning Sarah - Your Brief for Jan 7 | 4 Local Companies Today`
- `Hey Michael - Your Brief for Jan 7 | Strong Tech Sector Plays`

**Variables**:

- Time-appropriate greeting (Morning/Afternoon)
- User's first name
- Current date
- Key highlight (number of opportunities, top sector, etc.)

---

## Email Body (HTML + Plain Text Alternative)

### Section 1: Personal Greeting (Header)

```html
<div class="header">
  <h1>Good Morning, Alex! ☀️</h1>
  <p class="subtitle">
    Your personalized investment brief for Tuesday, January 7, 2026
  </p>

  <div class="weather-widget">
    <img src="weather-icon.png" alt="weather" />
    <span>16°C, Partly Cloudy | Auckland, New Zealand</span>
  </div>

  <div class="audio-player">
    🎧 <a href="{audio_url}">Listen to Your Voice Brief (4:32)</a>
  </div>
</div>
```

**Content**:

- Personalized greeting with user's name
- Current date and day of week
- Local weather (temperature, conditions, location)
- Embedded audio player link to voice briefing

---

### Section 2: Executive Summary

```html
<div class="executive-summary">
  <h2>Today's Brief Summary</h2>

  <div class="key-metrics">
    <div class="metric">
      <span class="number">10</span>
      <span class="label">Opportunities Found</span>
    </div>
    <div class="metric">
      <span class="number">4</span>
      <span class="label">Local Companies</span>
    </div>
    <div class="metric">
      <span class="number">8.7%</span>
      <span class="label">Avg Expected Return</span>
    </div>
    <div class="metric">
      <span class="number">7 days</span>
      <span class="label">Avg Timeframe</span>
    </div>
  </div>

  <div class="market-context">
    <h3>Market Context</h3>
    <ul>
      <li>NZX 50 opened up 0.7% tracking positive US sentiment</li>
      <li>Dairy prices rose 3.5% at GlobalDairyTrade auction</li>
      <li>Strong local employment data supports NZ equities</li>
    </ul>
  </div>
</div>
```

**Content**:

- Key metrics (opportunities, local count, avg return, timeframe)
- Brief market context (3-5 bullets)
- Overall sentiment assessment

---

### Section 3: Top Opportunities (Detailed Cards)

For each opportunity (Top 10), include a detailed card:

```html
<div class="opportunity-card" id="opportunity-1">
  <div class="card-header">
    <span class="rank">#1</span>
    <h3>a2 Milk Company (ATM.NZ)</h3>
    <span class="score">Score: 84/100</span>
  </div>

  <div class="card-badges">
    <span class="badge location">📍 8 km away</span>
    <span class="badge asset-type">Stock</span>
    <span class="badge risk">Moderate Risk</span>
  </div>

  <div class="recommendation">
    <div class="action"><strong>Recommendation:</strong> BUY</div>
    <div class="price-info">
      <span>Entry: <strong>NZ$6.45</strong></span>
      <span>Target: <strong>NZ$7.20</strong></span>
      <span>Stop Loss: <strong>NZ$6.00</strong></span>
    </div>
  </div>

  <div class="investment-calc">
    <table>
      <tr>
        <td>Suggested Investment:</td>
        <td><strong>NZ$50.00</strong></td>
      </tr>
      <tr>
        <td>Shares:</td>
        <td>~7.75 shares</td>
      </tr>
      <tr>
        <td>Expected Return:</td>
        <td class="positive">+NZ$5.80 (11.6%)</td>
      </tr>
      <tr>
        <td>Timeframe:</td>
        <td>7 days</td>
      </tr>
    </table>
  </div>

  <div class="chart">
    <img src="{price_chart_url}" alt="Price Chart" style="width: 100%;" />
  </div>

  <div class="why-now">
    <h4>Why Now?</h4>
    <ol>
      <li>
        <strong>Local Advantage:</strong> Headquartered 8 km from your location
        in Auckland. Recent hiring surge indicates business growth.
      </li>
      <li>
        <strong>Strong Fundamentals:</strong> Q4 revenue up 23% YoY driven by
        China market expansion.
      </li>
      <li>
        <strong>Technical Breakout:</strong> Breaking resistance at NZ$6.40 with
        strong volume.
      </li>
      <li>
        <strong>Positive Sentiment:</strong> 4 analyst upgrades this week, avg
        target NZ$7.20.
      </li>
    </ol>
  </div>

  <div class="supporting-evidence">
    <h4>Supporting Evidence</h4>
    <ul>
      <li>
        📰 <strong>News:</strong> "a2 Milk reports record China sales" - NZ
        Herald, Jan 5
      </li>
      <li>
        📊 <strong>Technical:</strong> RSI: 58 (bullish), MACD: Positive
        crossover
      </li>
      <li>
        👥 <strong>Analyst:</strong> Forsyth Barr upgraded to "Outperform" (Jan
        4)
      </li>
      <li>
        🏢 <strong>Local Intel:</strong> 12 new job postings at Auckland HQ this
        week
      </li>
    </ul>
  </div>

  <div class="risk-disclosure">
    <h4>⚠️ Risks to Consider</h4>
    <ul>
      <li>High dependence on China market (62% of revenue)</li>
      <li>Dairy price volatility</li>
      <li>Competitive pressure from established brands</li>
      <li>Historical volatility: 28% (High)</li>
    </ul>
  </div>

  <div class="fundamentals">
    <h4>Key Fundamentals</h4>
    <table class="fundamentals-table">
      <tr>
        <td>Market Cap:</td>
        <td>NZ$4.7B</td>
        <td>P/E Ratio:</td>
        <td>32.5</td>
      </tr>
      <tr>
        <td>Revenue Growth:</td>
        <td>23% YoY</td>
        <td>Profit Margin:</td>
        <td>8.2%</td>
      </tr>
      <tr>
        <td>Debt/Equity:</td>
        <td>0.15 (Low)</td>
        <td>Dividend Yield:</td>
        <td>1.2%</td>
      </tr>
    </table>
  </div>
</div>

<!-- Repeat for opportunities #2-10 -->
```

---

### Section 4: Asset Class Breakdown

```html
<div class="asset-breakdown">
  <h2>Opportunities by Asset Class</h2>

  <div class="breakdown-chart">
    <!-- Pie chart or bar chart -->
    <img src="{breakdown_chart_url}" alt="Asset Class Distribution" />
  </div>

  <table class="breakdown-table">
    <thead>
      <tr>
        <th>Asset Class</th>
        <th>Count</th>
        <th>Avg Score</th>
        <th>Avg Return</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Stocks (NZ)</td>
        <td>4</td>
        <td>81.5</td>
        <td>9.2%</td>
      </tr>
      <tr>
        <td>Forex</td>
        <td>2</td>
        <td>79.0</td>
        <td>6.5%</td>
      </tr>
      <tr>
        <td>Stocks (International)</td>
        <td>2</td>
        <td>75.5</td>
        <td>8.8%</td>
      </tr>
      <tr>
        <td>Cryptocurrency</td>
        <td>1</td>
        <td>73.0</td>
        <td>12.5%</td>
      </tr>
      <tr>
        <td>Commodities</td>
        <td>1</td>
        <td>70.0</td>
        <td>5.2%</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

### Section 5: Geographic Heatmap

```html
<div class="geographic-section">
  <h2>Geographic Distribution</h2>

  <div class="heatmap">
    <img src="{heatmap_url}" alt="Geographic Heatmap" />
  </div>

  <div class="proximity-stats">
    <h3>Proximity Breakdown</h3>
    <ul>
      <li>🏢 <strong>Hyper-Local (0-100km):</strong> 4 companies</li>
      <li>🌆 <strong>Regional (100-500km):</strong> 2 companies</li>
      <li>🌏 <strong>National (500-2000km):</strong> 1 company</li>
      <li>🌍 <strong>International (2000km+):</strong> 3 companies</li>
    </ul>
  </div>
</div>
```

---

### Section 6: Portfolio Impact (If User Has Tracked Portfolio)

```html
<div class="portfolio-section">
  <h2>Your Portfolio Insights</h2>

  <div class="current-portfolio">
    <h3>Current Holdings Performance</h3>
    <table>
      <thead>
        <tr>
          <th>Asset</th>
          <th>Cost Basis</th>
          <th>Current Value</th>
          <th>Return</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Tesla (TSLA)</td>
          <td>NZ$500.00</td>
          <td>NZ$511.50</td>
          <td class="positive">+2.3%</td>
        </tr>
        <!-- More holdings -->
      </tbody>
    </table>
  </div>

  <div class="diversification">
    <h3>Diversification Analysis</h3>
    <p>Today's recommendations would improve your portfolio diversification:</p>
    <ul>
      <li>Reduce tech sector concentration from 65% to 55%</li>
      <li>Add local NZ exposure (currently 0%)</li>
      <li>Increase forex diversification</li>
    </ul>
  </div>
</div>
```

---

### Section 7: Market Calendar & Events

```html
<div class="calendar-section">
  <h2>This Week's Key Events</h2>

  <table class="calendar">
    <thead>
      <tr>
        <th>Date</th>
        <th>Event</th>
        <th>Impact</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Jan 8</td>
        <td>🇺🇸 US CPI Data Release</td>
        <td class="high">High</td>
      </tr>
      <tr>
        <td>Jan 10</td>
        <td>🏦 RBNZ Interest Rate Decision</td>
        <td class="high">High</td>
      </tr>
      <tr>
        <td>Jan 12</td>
        <td>📊 Fisher & Paykel Earnings</td>
        <td class="medium">Medium</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

### Section 8: Educational Insights (Optional)

```html
<div class="education-section">
  <h2>💡 Today's Investment Insight</h2>

  <div class="insight-card">
    <h3>Understanding Location-Based Investing</h3>
    <p>
      Did you know? Studies show investors have a 2-3% information advantage
      when investing in companies within 100km of their location. This "home
      field advantage" comes from real-time observation of business activity,
      local news awareness, and cultural understanding.
    </p>
    <p>
      Today, 40% of your recommendations are local Auckland companies, giving
      you maximum informational edge.
    </p>
  </div>
</div>
```

---

### Section 9: Footer

```html
<div class="footer">
  <div class="disclaimer">
    <h4>⚠️ Important Disclaimer</h4>
    <p>
      This report is for informational and educational purposes only. It does
      not constitute financial advice. All investments carry risk, and past
      performance does not guarantee future results. Please consult with a
      licensed financial advisor before making investment decisions. Brief uses
      AI-powered analysis which may contain errors or omissions.
    </p>
  </div>

  <div class="actions">
    <a href="{app_deep_link}" class="button">Open in Brief App</a>
    <a href="{pdf_download_url}" class="button secondary"
      >Download PDF Report</a
    >
  </div>

  <div class="preferences">
    <p>
      <a href="{unsubscribe_url}">Unsubscribe</a> |
      <a href="{preferences_url}">Email Preferences</a> |
      <a href="{help_url}">Help & Support</a>
    </p>
  </div>

  <div class="branding">
    <p>© 2026 Brief - Your AI Investment Assistant</p>
    <p>Generated at 5:55 AM NZDT | Valid for 24 hours</p>
  </div>
</div>
```

---

## PDF Report Attachment

### PDF Structure

**Filename**: `Brief_Report_{Date}_{UserName}.pdf`
Example: `Brief_Report_2026-01-07_Alex.pdf`

**Page 1: Cover Page**

- Brief logo
- User name
- Date
- "Your Daily Investment Brief"
- QR code linking to audio briefing

**Pages 2-3: Executive Summary**

- Same as email executive summary
- Market context
- Key metrics

**Pages 4-15: Opportunity Details**

- One page per opportunity (top 10)
- Full details with charts
- Supporting evidence
- Risk disclosures

**Page 16: Asset Allocation Recommendation**

- Pie chart of suggested allocation
- Risk-adjusted portfolio suggestions

**Page 17: Geographic Analysis**

- Heatmap
- Distance calculations
- Proximity advantages

**Page 18: Appendix**

- Methodology explanation
- Data sources
- Glossary of terms
- Disclaimer

**Formatting**:

- Professional typography (fonts: Inter, SF Pro)
- Color-coded risk levels
- High-quality charts and graphs
- Print-friendly (black & white compatible)

---

## Email Personalization Variables

### User-Specific

- `{user_name}` - First name
- `{user_full_name}` - Full name
- `{user_location}` - City, Country
- `{user_timezone}` - Timezone
- `{briefing_time}` - Scheduled time

### Weather

- `{weather_temp}` - Temperature
- `{weather_condition}` - Clear, Cloudy, etc.
- `{weather_icon}` - Icon URL

### Market Data

- `{market_index}` - Main local index (NZX 50, S&P 500, etc.)
- `{market_change}` - % change
- `{market_sentiment}` - Bullish/Bearish/Neutral

### Performance

- `{opportunities_count}` - Number of opportunities
- `{local_count}` - Number of local opportunities
- `{avg_expected_return}` - Average expected return %
- `{avg_timeframe}` - Average investment timeframe

---

## Email Timing

### Sending Schedule

**Primary Delivery**:

- Sent at T+0 (briefing time, e.g., 6:00 AM)
- Simultaneously with push notification
- High priority delivery

**Retry Logic**:

- If email bounces, retry 3 times (5 min intervals)
- If user's inbox is full, queue for later
- Log delivery failures for investigation

**Time Zone Handling**:

- All times in user's local timezone
- Daylight saving time aware
- Consistent with user's briefing schedule

---

## Email Templates

### Multiple Template Options

Users can choose email style:

**1. Detailed (Default)**

- Full analysis as described above
- All 10 opportunities
- ~15-20 min read time

**2. Executive**

- Top 3 opportunities only
- Brief summaries
- ~5 min read time

**3. Digest**

- Bullet-point format
- Key metrics only
- Links to full report
- ~2 min read time

**4. Mobile-Optimized**

- Single column layout
- Larger fonts
- Simplified charts
- Perfect for phone reading

---

## Technical Specifications

### Email Service

- **Provider**: SendGrid or AWS SES
- **From Address**: `brief@brief-app.com`
- **From Name**: `Brief - Your AI Assistant`
- **Reply-To**: `support@brief-app.com`

### HTML/CSS Requirements

- Responsive design (mobile-first)
- Email client compatible (Gmail, Outlook, Apple Mail)
- Inline CSS (no external stylesheets)
- Alt text for all images
- Plain text fallback version

### Attachments

- **PDF**: Max 5 MB
- **Compression**: Optimized images
- **Accessibility**: PDF/UA compliant

### Tracking

- **Open Tracking**: Pixel-based
- **Click Tracking**: Link wrapping
- **Unsubscribe**: One-click unsubscribe (RFC 8058)

### Analytics

Track:

- Open rate
- Click-through rate (by opportunity)
- Time to open after delivery
- PDF download rate
- Audio play rate

---

## Sample Email Preview

```
Subject: Good Morning Alex - Your Brief for Jan 7 | 10 Opportunities Found

═══════════════════════════════════════════════════════════
                        BRIEF
        Your AI-Powered Investment Intelligence
═══════════════════════════════════════════════════════════

Good Morning, Alex! ☀️

Your personalized investment brief for Tuesday, January 7, 2026

Weather in Auckland: 16°C, Partly Cloudy

🎧 Listen to Your Voice Brief (4:32) → [PLAY NOW]

═══════════════════════════════════════════════════════════

TODAY'S BRIEF SUMMARY

    10              4               8.7%           7 days
Opportunities    Local          Avg Expected    Avg Timeframe
   Found       Companies          Return

MARKET CONTEXT:
• NZX 50 opened up 0.7% tracking positive US sentiment
• Dairy prices rose 3.5% at GlobalDairyTrade auction
• Strong local employment data supports NZ equities

═══════════════════════════════════════════════════════════

#1 a2 Milk Company (ATM.NZ)                    Score: 84/100

📍 8 km away | Stock | Moderate Risk

RECOMMENDATION: BUY at NZ$6.45
Target: NZ$7.20 | Stop Loss: NZ$6.00

Suggested Investment: NZ$50.00 (~7.75 shares)
Expected Return: +NZ$5.80 (11.6%) in 7 days

[PRICE CHART]

WHY NOW?
1. Local Advantage: HQ 8 km away. Hiring surge detected.
2. Strong Fundamentals: Q4 revenue up 23% YoY
3. Technical Breakout: Breaking NZ$6.40 resistance
4. Positive Sentiment: 4 analyst upgrades this week

[READ MORE →]

───────────────────────────────────────────────────────────
[Opportunities #2-10...]
───────────────────────────────────────────────────────────

[Open in Brief App] [Download PDF Report]

⚠️ Disclaimer: This report is for informational purposes only...

═══════════════════════════════════════════════════════════
```

---

This comprehensive email report gives users everything they need to make informed investment decisions while complementing the quick, convenient voice briefing! 📧
