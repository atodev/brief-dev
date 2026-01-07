# Daily Briefing Compilation Process

## Overview

The "Brief" application generates personalized, location-aware investment recommendations on a user-defined schedule. This document details the compilation process, timing requirements, and location-based prioritization algorithm.

---

## Timing & Scheduling

### User Configuration

Users set their preferred briefing time during onboarding:

- **Briefing Time**: e.g., 6:00 AM local time
- **Timezone**: Automatically detected or manually selected
- **Frequency**: Daily, weekdays only, or custom schedule
- **Lead Time**: System requires **60 minutes** to compile briefing

### Compilation Timeline

For a **6:00 AM briefing**, the process begins at **5:00 AM**:

```
5:00:00 AM - Scheduler triggers briefing job
5:00:15 AM - Briefing Service initializes
5:01:00 AM - Data collection phase begins
5:10:00 AM - AI analysis phase begins
5:25:00 AM - Location prioritization begins
5:35:00 AM - Evidence generation begins
5:45:00 AM - Final assembly begins
5:55:00 AM - Briefing cached and ready
5:58:00 AM - Push notification sent
6:00:00 AM - User receives notification
```

---

## Detailed Phase Breakdown

### Phase 1: Initialization (0-1 minute)

**Time**: T-60 to T-59 minutes

**Actions**:

1. Scheduler Service checks all users with briefings scheduled for current hour
2. Creates job queue entries for each user
3. Briefing Service picks up jobs from queue
4. Loads user profile, preferences, and location data

**Data Retrieved**:

- User ID and authentication context
- Location (latitude, longitude, timezone)
- Risk profile (conservative, moderate, aggressive)
- Investment preferences (asset classes, sectors)
- Available capital for investment
- Existing portfolio positions
- Briefing history and past actions

**Database Queries**: ~10-15 queries to PostgreSQL
**Processing Time**: 30-60 seconds per user

---

### Phase 2: Market Data Collection (2-10 minutes)

**Time**: T-59 to T-50 minutes

**Actions**:

1. Check Redis cache for recent market data
2. Fetch fresh data for all tracked assets across 5 market types
3. Collect 24-hour price history for technical analysis
4. Update internal time-series database

**Data Sources**:

#### Cryptocurrency (2 minutes)

- Binance API: Top 50 cryptocurrencies by market cap
- CoinGecko: Market overview, volume, dominance
- **API Calls**: ~100-150 requests
- **Data Points**: ~10,000 OHLCV candles

#### Forex (1.5 minutes)

- OANDA API: Major and minor pairs (20-30 pairs)
- Alpha Vantage: Daily rates and trends
- **API Calls**: ~40-60 requests
- **Data Points**: ~500 price points

#### Stocks (3 minutes)

- Polygon.io: US markets (S&P 500, NASDAQ 100)
- IEX Cloud: Real-time quotes
- Yahoo Finance: International markets
- **API Calls**: ~200-300 requests
- **Data Points**: ~50,000 OHLCV candles

#### Commodities (1.5 minutes)

- Quandl: Gold, silver, oil, natural gas, agricultural
- **API Calls**: ~20-30 requests
- **Data Points**: ~200 price points

#### Prediction Markets (2 minutes)

- Polymarket API: Active markets with high volume
- **API Calls**: ~50-100 requests
- **Data Points**: ~500 market odds

**Total API Calls**: 410-640 calls
**Data Cached**: 70-80% from previous compilations
**Fresh Data**: 20-30% requires new API calls
**Processing Time**: 8-10 minutes

---

### Phase 3: News & Sentiment Collection (5 minutes)

**Time**: T-50 to T-45 minutes

**Actions**:

1. Fetch news articles from last 24 hours
2. Filter by relevance to tracked assets
3. Extract key events (earnings, regulations, partnerships)
4. Collect social media sentiment

**Data Sources**:

#### News Articles (3 minutes)

- NewsAPI: Financial news from 100+ sources
- Benzinga: Stock-specific news
- Reuters: Breaking financial news
- **API Calls**: ~150-200 requests
- **Articles Collected**: ~500-1000 articles
- **Filtered Articles**: ~100-200 relevant articles

#### Social Sentiment (2 minutes)

- Twitter API: Mentions of tracked assets
- Reddit API: r/wallstreetbets, r/investing, r/cryptocurrency
- **API Calls**: ~100-150 requests
- **Posts Analyzed**: ~2000-5000 posts

**Processing**:

- NLP preprocessing (tokenization, cleaning)
- Entity recognition (company names, tickers)
- Sentiment classification (positive/negative/neutral)
- Event extraction (M&A, earnings, regulatory)

**Processing Time**: 5 minutes

---

### Phase 4: AI Model Inference (15 minutes)

**Time**: T-45 to T-30 minutes

This is the most compute-intensive phase. Models run in parallel on GPU instances.

#### 4.1 Price Prediction Models (6 minutes)

**Models**:

- LSTM networks for crypto and stocks
- ARIMA for forex
- Technical indicator analysis (RSI, MACD, Bollinger Bands)

**Input**:

- Historical price data (30-90 days)
- Volume data
- Technical indicators

**Output**:

- Price predictions (1-day, 7-day, 30-day)
- Confidence intervals
- Trend direction (bullish/bearish/neutral)

**Assets Analyzed**: ~1000-2000 assets
**Predictions Generated**: ~6000-12000 predictions (3 timeframes each)
**Processing Time**: 6 minutes on GPU instance (AWS P3)

#### 4.2 Sentiment Analysis (4 minutes)

**Models**:

- FinBERT for financial text
- Custom transformer for social media

**Input**:

- 100-200 news articles
- 2000-5000 social media posts

**Output**:

- Sentiment scores (-1 to +1)
- Entity-specific sentiment
- Event impact scores

**Processing Time**: 4 minutes on GPU instance

#### 4.3 Risk Assessment (3 minutes)

**Models**:

- Volatility prediction (GARCH)
- Correlation analysis
- Portfolio risk metrics (VaR, CVaR)

**Input**:

- Historical volatility
- Current portfolio composition
- User risk profile

**Output**:

- Risk scores (0-100)
- Volatility forecasts
- Correlation matrices

**Processing Time**: 3 minutes

#### 4.4 Pattern Recognition (2 minutes)

**Models**:

- Chart pattern detection (CNNs)
- Anomaly detection (autoencoders)

**Input**:

- Price charts (candlestick images)
- Volume patterns

**Output**:

- Detected patterns (head & shoulders, triangles, etc.)
- Anomaly alerts
- Breakout probabilities

**Processing Time**: 2 minutes

**Total AI Processing**: 15 minutes (parallelized across models)
**Compute Cost**: ~$0.50-1.00 per briefing (GPU time)

---

### Phase 5: Location-Based Prioritization (10 minutes)

**Time**: T-30 to T-20 minutes

This is the **unique differentiator** of the Brief app.

#### 5.1 Company Location Mapping (2 minutes)

**Actions**:

1. Retrieve company headquarters locations from database
2. For crypto/forex, map to primary exchange location
3. For commodities, map to production/trading regions

**Data Structure**:

```json
{
  "asset_id": "AAPL",
  "company_name": "Apple Inc.",
  "headquarters": {
    "latitude": 37.3349,
    "longitude": -122.009,
    "address": "Cupertino, CA, USA"
  },
  "primary_exchange": "NASDAQ",
  "exchange_location": {
    "latitude": 40.7128,
    "longitude": -74.006,
    "timezone": "America/New_York"
  }
}
```

**Database**: PostgreSQL with PostGIS extension
**Query Time**: 1-2 minutes for ~1000 assets

#### 5.2 Distance Calculation (3 minutes)

**Algorithm**: Haversine formula for geographic distance

```python
def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate great-circle distance between two points on Earth
    Returns distance in kilometers
    """
    R = 6371  # Earth radius in km

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))

    return R * c
```

**Calculation**:

- Calculate distance from user location to each asset's HQ
- Calculate distance to primary exchange
- Use minimum of the two distances

**Processing**: Vectorized computation for ~1000 assets
**Time**: 2-3 minutes

#### 5.3 Geographic Tier Assignment (1 minute)

**Categories**:

- **Tier 1 - Hyper-Local** (0-100 km): 100% location weight
  - Example: User in San Francisco, companies in Bay Area
  - Same metro area, immediate economic impact
- **Tier 2 - Regional** (100-500 km): 75% location weight
  - Example: User in San Francisco, companies in Los Angeles
  - Same state or neighboring states
- **Tier 3 - National** (500-2000 km): 50% location weight
  - Example: User in San Francisco, companies in New York
  - Same country, different region
- **Tier 4 - International** (2000+ km): 25% location weight
  - Example: User in San Francisco, companies in London
  - Different country/continent

**Output**: Each asset tagged with geographic tier

#### 5.4 Market Hours Overlap (2 minutes)

**Calculation**:

```python
def calculate_market_overlap(user_tz, exchange_tz):
    """
    Calculate percentage of market hours that overlap
    with user's waking hours (6 AM - 11 PM)
    """
    user_awake_start = 6  # 6 AM local time
    user_awake_end = 23   # 11 PM local time

    # Convert exchange market hours to user timezone
    market_open_user_tz = convert_timezone(
        9.5,  # 9:30 AM exchange time
        exchange_tz,
        user_tz
    )
    market_close_user_tz = convert_timezone(
        16.0,  # 4:00 PM exchange time
        exchange_tz,
        user_tz
    )

    # Calculate overlap
    overlap_start = max(user_awake_start, market_open_user_tz)
    overlap_end = min(user_awake_end, market_close_user_tz)

    if overlap_end <= overlap_start:
        return 0  # No overlap

    overlap_hours = overlap_end - overlap_start
    market_hours = 6.5  # Standard trading hours

    return overlap_hours / market_hours
```

**Why This Matters**:

- Higher overlap = easier to monitor and react to market movements
- Crypto trades 24/7, so gets neutral score
- Asian markets get lower score for US-based users

**Processing Time**: 2 minutes for ~1000 assets

#### 5.5 Local Economic Impact (2 minutes)

**Factors Considered**:

- Is the company a major local employer?
- Does the company have operations in user's region?
- Local economic indicators (GDP, unemployment) correlation
- Regional industry concentration

**Data Sources**:

- Company employment data
- FRED (Federal Reserve Economic Data) for regional indicators
- Company facility locations

**Scoring**:

- Major local employer: +10 points
- Regional operations: +5 points
- High regional economic correlation: +5 points

**Processing Time**: 2 minutes

#### 5.6 Final Location Score Calculation (1 minute)

**Formula**:

```python
location_score = (
    geographic_tier_weight * 40% +      # 40% proximity
    market_overlap_score * 30% +        # 30% market hours
    local_economic_impact * 20% +       # 20% local impact
    user_familiarity_bonus * 10%        # 10% user familiarity
)
```

**User Familiarity Bonus**:

- User has previously invested in this asset: +10 points
- User has this asset on watchlist: +5 points
- User lives/works near company: +15 points

**Output**: Location score (0-100) for each asset

**Total Phase 5 Time**: 10 minutes

---

### Phase 6: Combined Scoring & Ranking (5 minutes)

**Time**: T-20 to T-15 minutes

#### 6.1 Aggregate Scoring

**Formula**:

```python
final_score = (
    ai_prediction_score * 35% +        # 35% ML predictions
    sentiment_score * 20% +            # 20% sentiment
    technical_score * 15% +            # 15% technical indicators
    location_score * 25% +             # 25% location proximity
    risk_adjusted_return * 5%          # 5% risk adjustment
)
```

**Location Weight Configurable**:
Users can adjust location preference:

- **Heavy Local Focus**: 40% location weight (reduce AI to 25%)
- **Balanced** (Default): 25% location weight
- **Ignore Location**: 0% location weight (distribute to AI)

#### 6.2 Filtering

**Remove Assets That**:

- Fall below minimum score threshold (e.g., 60/100)
- Have high correlation with existing portfolio (over-concentration)
- Exceed user's risk tolerance
- Have insufficient liquidity
- Are restricted by user's location/regulations
- Have negative news events (bankruptcy, fraud)

**Typical Filtering Results**:

- Starting pool: ~1000 assets analyzed
- After filtering: ~100-200 assets remain

#### 6.3 Diversification Check

**Ensure Recommendations Include**:

- Multiple asset classes (crypto, stocks, forex, etc.)
- Multiple sectors (tech, healthcare, energy, etc.)
- Multiple geographic tiers (not all local)
- Mix of risk levels (conservative + aggressive)

**Algorithm**: Greedy diversification selector

#### 6.4 Top N Selection

**Select Top Opportunities**:

- **Top 10**: Displayed prominently in app
- **Top 20**: Available with "see more" expansion
- **Top 50**: Available in detailed view

**Sort By**:

1. Final score (descending)
2. Risk-adjusted return (for ties)
3. Location proximity (for further ties)

**Processing Time**: 5 minutes

---

### Phase 7: Evidence Generation (10 minutes)

**Time**: T-15 to T-5 minutes

For each of the **Top 10** recommendations, generate detailed supporting evidence.

#### 7.1 Fundamental Analysis (3 minutes)

**For Stocks**:

- P/E ratio, P/B ratio, debt/equity
- Revenue growth, profit margins
- Analyst ratings and price targets
- Upcoming earnings dates

**For Crypto**:

- Market cap, circulating supply
- Network metrics (active addresses, transaction volume)
- Recent protocol upgrades or partnerships

**For Forex**:

- Interest rate differentials
- Economic indicators (GDP, inflation, unemployment)
- Central bank policies

**Data Sources**: Financial Modeling Prep, IEX Cloud, CoinGecko

#### 7.2 Technical Analysis Summary (2 minutes)

**Key Indicators**:

- Current trend (short, medium, long-term)
- Support and resistance levels
- Momentum indicators (RSI, MACD)
- Volume profile

**Chart Patterns**:

- Detected patterns and their historical success rates
- Breakout levels and targets

#### 7.3 News & Catalyst Summary (3 minutes)

**Extract Key Information**:

- Recent news headlines (last 24-48 hours)
- Upcoming events (earnings, product launches, conferences)
- Regulatory developments
- Major partnerships or acquisitions

**Summarization**:

- Use OpenAI GPT-4 or Anthropic Claude to generate concise summaries
- Extract key quotes from articles
- Identify catalysts (events that could move price)

**API Calls**: 10 LLM requests (one per recommendation)
**Cost**: ~$0.05-0.10 per briefing

#### 7.4 Risk Disclosure (1 minute)

**For Each Recommendation**:

- Volatility level (high/medium/low)
- Maximum historical drawdown
- Key risks (regulatory, competitive, technological)
- Correlation with user's existing portfolio

#### 7.5 "Why Now?" Reasoning (1 minute)

**AI-Generated Explanation**:

```
Example Output:
"Apple (AAPL) is recommended today because:

1. Location Advantage: Headquartered 15 km from your location in
   San Jose, CA, giving you real-time awareness of local developments.

2. Technical Breakout: Price broke above 200-day moving average
   yesterday with strong volume, indicating bullish momentum.

3. Positive Sentiment: 3 positive analyst upgrades this week, with
   average price target of $185 (+8% from current).

4. Upcoming Catalyst: Q1 earnings report in 5 days, with expectations
   for strong iPhone sales.

5. Your Portfolio Fit: Low correlation (0.3) with your existing tech
   holdings, improving diversification."
```

**Generation**: Template-based + LLM enhancement
**Processing Time**: 10 minutes for top 10 recommendations

---

### Phase 8: Final Assembly (10 minutes)

**Time**: T-10 to T-0

#### 8.1 Briefing Structure Creation (2 minutes)

**Format**:

```json
{
  "user_id": "user_123",
  "briefing_date": "2026-01-07",
  "briefing_time": "06:00:00",
  "timezone": "America/Los_Angeles",
  "generation_time": "05:55:23",
  "market_summary": {
    "overnight_changes": "...",
    "local_market_status": "...",
    "global_highlights": "..."
  },
  "top_opportunities": [
    {
      "rank": 1,
      "asset_id": "AAPL",
      "asset_name": "Apple Inc.",
      "asset_type": "stock",
      "current_price": 172.45,
      "recommended_action": "BUY",
      "suggested_amount": 1500.00,
      "expected_return": 8.5,
      "timeframe": "7 days",
      "final_score": 87.3,
      "location_proximity": "15 km (Hyper-Local)",
      "reasoning": "...",
      "supporting_evidence": {...},
      "risks": [...],
      "entry_price": 172.50,
      "target_price": 187.00,
      "stop_loss": 165.00
    },
    // ... 9 more opportunities
  ],
  "portfolio_insights": {...},
  "market_alerts": [...]
}
```

#### 8.2 Visualization Generation (3 minutes)

**Create**:

- Mini price charts for each recommendation (sparklines)
- Geographic heat map showing opportunity distribution
- Portfolio allocation pie chart
- Risk vs. return scatter plot

**Technology**: Chart.js or D3.js pre-rendering
**Storage**: Images stored in S3, URLs in briefing JSON

#### 8.3 Compliance Checks (2 minutes)

**Verify**:

- No restricted securities for user's jurisdiction
- Disclosure text included for high-risk assets
- Terms of service acceptance is current
- User has sufficient account balance
- No regulatory holds on user account

**Compliance Service**: Validates each recommendation
**Action**: Remove non-compliant recommendations, flag issues

#### 8.4 Personalization (2 minutes)

**Customize**:

- Greeting with user's name
- Reference previous briefings if user acted on recommendations
- Adjust tone based on user preferences (formal vs. casual)
- Language translation if needed

**Example**:

```
Good morning, Alex!

Yesterday you invested in Tesla (TSLA) from your briefing.
It's up 2.3% - great timing!

Today we've found 10 new opportunities, with 4 companies
headquartered right here in Silicon Valley...
```

#### 8.5 Caching (1 minute)

**Store in Redis**:

- Key: `briefing:user_{user_id}:{date}`
- TTL: 24 hours
- Format: Compressed JSON
- Size: ~100-500 KB per briefing

**Total Phase 8 Time**: 10 minutes

---

### Phase 9: Notification & Delivery (0-2 minutes)

**Time**: T-2 to T-0

#### 9.1 Push Notification (1 minute)

**Send via Firebase Cloud Messaging**:

- **Title**: "Your Brief is Ready 📊"
- **Body**: "10 opportunities found. 4 local companies within 50km."
- **Action**: Deep link to briefing screen in app
- **Priority**: High (ensures immediate delivery)

#### 9.2 Email Summary (optional, 1 minute)

**If User Enabled**:

- Send email with brief summary
- Top 3 recommendations
- Link to full briefing in app

#### 9.3 Logging (< 1 second)

**Record**:

- Briefing generation success
- Total processing time
- Number of recommendations
- Any errors or warnings

**Total Phase 9 Time**: 1-2 minutes

---

## Total Time Summary

| Phase                      | Duration | Cumulative Time |
| -------------------------- | -------- | --------------- |
| 1. Initialization          | 1 min    | 1 min           |
| 2. Market Data Collection  | 8-10 min | 11 min          |
| 3. News & Sentiment        | 5 min    | 16 min          |
| 4. AI Model Inference      | 15 min   | 31 min          |
| 5. Location Prioritization | 10 min   | 41 min          |
| 6. Scoring & Ranking       | 5 min    | 46 min          |
| 7. Evidence Generation     | 10 min   | 56 min          |
| 8. Final Assembly          | 10 min   | 66 min          |
| 9. Notification            | 2 min    | 68 min          |

**Total: 60-70 minutes**
**Recommended Buffer: +10 minutes for peak load**
**Safe Lead Time: 1 hour before briefing time**

---

## Scalability Considerations

### For 1,000 Users (All 6 AM Briefings)

**Challenge**: All briefings start at 5 AM

**Solution**:

1. **Stagger Start Times**: Spread job starts across 5:00-5:20 AM
2. **Shared Data**: Market data collected once, shared across users
3. **Parallel Processing**: Multiple worker nodes process briefings simultaneously
4. **Resource Scaling**: Auto-scale GPU instances at 5 AM

**Cost**:

- Market data collection: $1-2 (shared)
- Per-user AI processing: $0.50-1.00 × 1,000 = $500-1,000
- LLM calls: $0.10 × 1,000 = $100
- **Total: ~$600-1,100 per hour**

### For 100,000 Users (Various Times)

**Challenge**: Continuous briefing generation

**Solution**:

1. **24/7 Worker Pool**: Maintain pool of workers across timezones
2. **Smart Caching**: Cache common data (S&P 500 analysis, news summaries)
3. **Priority Queue**: Premium users get faster processing
4. **Pre-computation**: Start data collection 2 hours early, run models ahead

**Infrastructure**:

- 20-50 worker nodes
- 10-20 GPU instances
- Large Redis cluster (100+ GB)
- High-throughput message queue

**Cost**: $15,000-30,000 per day for AI processing

---

## Optimization Strategies

### 1. Incremental Updates

**Instead of full recompilation**:

- Cache previous day's briefing
- Only re-analyze assets with significant changes (>5% price move, major news)
- Reuse location calculations (don't change often)
- **Time Saved**: 20-30 minutes → **30-40 minute total time**

### 2. Pre-computation

**Run analysis continuously**:

- Market data updated every 5 minutes
- AI models run every 30 minutes on new data
- Briefing generation is just assembly + personalization
- **Time Saved**: 40-50 minutes → **10-20 minute total time**

### 3. User Tiers

**Different SLA by subscription**:

- **Free Tier**: 2-hour lead time, simplified analysis
- **Premium**: 1-hour lead time, full analysis
- **Pro**: 30-minute lead time, priority processing

---

## Fallback & Error Handling

### If Briefing Fails to Generate in Time

**Fallback Strategy**:

1. Use previous day's briefing with disclaimer
2. Generate simplified briefing (top 5 instead of 10)
3. Delay notification by 15-30 minutes
4. Alert engineering team

### If External APIs are Down

**Redundancy**:

- Primary + backup data sources for each market type
- Cached data from previous hours
- Graceful degradation (skip affected asset class)

### If AI Models Fail

**Fallback**:

- Use simpler rule-based algorithms
- Rely more on technical indicators (no ML needed)
- Show disclaimer: "Briefing generated with limited AI"

---

## Future Enhancements

### 1. Faster Compilation (Target: 15 minutes)

- **Edge ML Models**: Deploy lightweight models closer to users
- **Real-time Streaming**: Continuous analysis instead of batch
- **Model Distillation**: Smaller, faster models with similar accuracy

### 2. More Granular Location Awareness

- **Neighborhood-Level**: Prioritize companies in user's neighborhood
- **Commute Routes**: Favor companies along user's commute
- **Visited Locations**: Consider places user frequently visits
- **Real-time Location**: Update priorities based on current location

### 3. Event-Driven Briefings

- **Breaking News**: Immediate briefing when major event occurs locally
- **Market Volatility**: Special briefings during high volatility
- **Portfolio Alerts**: Instant briefings when holdings move significantly

### 4. Conversational Briefings

- **Voice Interface**: Listen to briefing while getting ready
- **Q&A**: Ask follow-up questions about recommendations
- **Real-time Updates**: Briefing updates as user commutes to work

---

## Conclusion

**Answer to Original Question**:

> "How much time would the AI require to compile a list of actionable investments prior to the brief?"

**Answer**:

- **Minimum: 60 minutes** (with all optimizations)
- **Recommended: 90 minutes** (with safety buffer)
- **Conservative: 120 minutes** (for peak load times)

For a **6:00 AM briefing**, we recommend scheduling compilation to start at **4:30-5:00 AM** to ensure reliable, high-quality recommendations with location-aware prioritization.
