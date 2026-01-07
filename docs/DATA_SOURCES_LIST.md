# Data Sources Interrogated Before Each Brief

## Overview

Before your 6:00 AM briefing, Brief interrogates **50+ data sources** across multiple categories to compile comprehensive investment intelligence. This document lists every resource queried during the briefing generation process.

---

## Briefing Compilation: Data Sources by Phase

### Phase 1: User Context (T-60 min)

**User Database (PostgreSQL)**

- User profile and preferences
- Location (city, coordinates, timezone)
- Risk tolerance profile
- Investment preferences (asset classes, sectors)
- Portfolio holdings (if tracked)
- Historical briefing actions
- Subscription tier

**Weather API**

- OpenWeatherMap API
- Current conditions at user location
- Temperature, conditions, forecast
- Used for personalized greeting

---

### Phase 2: Market Data Collection (T-59 to T-50 min)

#### Cryptocurrency Data (5 sources)

**1. Binance API**

- Real-time prices (50+ cryptocurrencies)
- 24-hour volume
- Order book depth
- Recent trades
- Funding rates (futures)
- WebSocket: Live price feeds

**2. CoinGecko API**

- Market cap rankings
- Price history (24h, 7d, 30d, 90d)
- Total market cap
- Bitcoin dominance
- Trading volume across exchanges
- DeFi protocol data

**3. Coinbase Advanced Trade API**

- US market prices
- Institutional order flow
- Premium/discount vs other exchanges
- Trading pairs availability

**4. CryptoCompare API**

- Historical OHLCV data
- Social media metrics
- Mining data
- Blockchain metrics

**5. Glassnode (Optional/Premium)**

- On-chain metrics
- Whale wallet movements
- Exchange inflows/outflows
- Network activity

---

#### Forex Data (3 sources)

**1. OANDA API**

- Real-time FX rates
- 120+ currency pairs
- Bid/ask spreads
- Historical rates (tick, 1m, 5m, 1h, daily)

**2. Alpha Vantage**

- Major currency pairs
- Technical indicators pre-calculated
- Digital currency exchange rates
- Economic calendar

**3. Twelve Data**

- Intraday forex data
- Cross rates
- Exotic pairs
- Technical indicators

---

#### Stock Market Data (5 sources)

**1. Yahoo Finance (yfinance)**

- US stocks (S&P 500, NASDAQ 100, Dow 30)
- International markets (NZX 50, ASX 200, FTSE, DAX)
- Historical prices (daily, 5y history)
- Dividends and splits
- Company info

**2. IEX Cloud**

- Real-time US stock quotes
- Pre-market and after-hours
- Company news
- Financials
- Analyst ratings
- Earnings calendar

**3. Polygon.io**

- Tick-level data
- Aggregated bars (1m, 5m, 1h, daily)
- Options data
- Market status
- Stock splits

**4. Finnhub**

- Real-time quotes
- Company news
- Earnings estimates
- Insider transactions
- IPO calendar

**5. Financial Modeling Prep**

- Financial statements (10-K, 10-Q)
- Key metrics (P/E, P/B, ROE, etc.)
- DCF valuations
- Historical ratios (5+ years)

---

#### Commodities Data (2 sources)

**1. Quandl (Nasdaq Data Link)**

- Gold, silver prices
- Crude oil (WTI, Brent)
- Natural gas
- Agricultural commodities (wheat, corn, soybeans)
- Historical data (20+ years)

**2. Alpha Vantage Commodities**

- WTI crude oil
- Brent crude oil
- Natural gas
- Copper, aluminum
- Coffee, wheat, corn, cotton, sugar

---

#### Prediction Markets (2 sources)

**1. Polymarket API**

- Active prediction markets
- Current odds
- Trading volume
- Market resolution dates
- Historical odds

**2. Augur (optional)**

- Decentralized prediction markets
- Event outcomes
- Market liquidity

---

#### Indices & ETFs

**Global Indices** (via multiple sources):

- US: S&P 500, NASDAQ 100, Dow Jones, Russell 2000
- NZ: NZX 50
- Australia: ASX 200
- Europe: FTSE 100, DAX, CAC 40
- Asia: Nikkei 225, Hang Seng, Shanghai Composite

**ETFs Tracked**:

- SPY, QQQ (US equity)
- GLD, SLV (precious metals)
- USO, UNG (energy)
- TLT (bonds)
- EEM (emerging markets)

---

### Phase 3: News & Sentiment (T-50 to T-45 min)

#### News Sources (7 sources)

**1. NewsAPI**

- 80,000+ news sources
- Financial news category
- Company-specific articles
- Last 24 hours
- Keyword filtering

**2. Benzinga News API**

- Real-time financial news
- Earnings announcements
- Analyst ratings
- M&A activity
- FDA approvals

**3. Reuters (via Finnhub)**

- Breaking financial news
- Global markets coverage
- Economic policy news

**4. Bloomberg Terminal API (Premium/Optional)**

- Professional-grade news
- Analyst reports
- Market commentary
- Corporate actions

**5. Company Press Releases**

- Direct from investor relations sites
- Scraped via web crawlers
- SEC Edgar filings (8-K, 10-K, 10-Q)

**6. Financial Times (Web Scraping)**

- Global financial news
- Market analysis
- Economic commentary

**7. Local NZ News** (for NZ users)

- NZ Herald Business
- Stuff.co.nz Business
- BusinessDesk
- NBR (National Business Review)

---

#### Social Media Sources (5 sources)

**1. Twitter/X API**

- Mentions of tracked assets
- Hashtag trends (#Bitcoin, #stocks, etc.)
- Influencer tweets (verified accounts)
- Sentiment analysis
- Retweet/like counts

**2. Reddit API**

- r/wallstreetbets
- r/investing
- r/stocks
- r/cryptocurrency
- r/forex
- Post sentiment
- Upvote counts
- Comment analysis

**3. StockTwits**

- Ticker-specific sentiment
- Bullish/bearish indicators
- Message volume
- Trending tickers

**4. Discord (Public Servers)**

- Crypto Discord servers
- Trading communities
- Sentiment extraction

**5. Telegram (Public Channels)**

- Crypto trading signals
- Market discussion groups

---

### Phase 4: Alternative Data (T-50 to T-45 min)

#### Satellite Imagery (2 sources)

**1. Planet Labs**

- Daily satellite imagery
- Oil storage facilities
- Retail parking lots
- Manufacturing facilities
- Port congestion
- Agricultural crop health

**2. Maxar Technologies**

- High-resolution imagery
- Infrastructure monitoring
- Industrial activity
- Construction progress

---

#### Supply Chain Intelligence (3 sources)

**1. MarineTraffic**

- Real-time ship positions (AIS data)
- 500,000+ vessels tracked
- Port arrivals/departures
- Shipping routes
- Cargo types

**2. FleetMon**

- Vessel tracking
- Port congestion metrics
- Shipping delays
- Fleet utilization

**3. FreightWaves SONAR**

- Trucking capacity
- Shipping rates
- Supply chain bottlenecks

---

#### Consumer Behavior (3 sources)

**1. SafeGraph**

- Foot traffic to stores
- Visit duration
- Visitor demographics
- Store performance metrics

**2. Placer.ai**

- Retail foot traffic
- Competitive analysis
- Trade area analysis

**3. Second Measure (Credit Cards)**

- Transaction volume
- Average ticket size
- Customer retention
- Market share trends

---

#### Web Scraping & Signals (5 sources)

**1. LinkedIn (Job Postings)**

- New job listings
- Company hiring trends
- Department expansion
- Seniority levels

**2. Indeed (Job Postings)**

- Job posting volumes
- Salary trends
- Geographic hiring

**3. App Annie / Sensor Tower**

- App download rankings
- App store reviews
- User ratings
- Revenue estimates

**4. Company Websites**

- Product availability
- Pricing changes
- Store locations
- Career pages

**5. E-commerce Scraping**

- Amazon product availability
- Pricing trends
- Review sentiment
- Sales rank

---

### Phase 5: Economic Data (T-50 to T-45 min)

#### Government Sources (4 sources)

**1. FRED (Federal Reserve Economic Data)**

- GDP growth
- Inflation (CPI, PCE)
- Unemployment rate
- Interest rates
- Money supply
- Consumer confidence

**2. Reserve Bank of New Zealand**

- Official Cash Rate (OCR)
- Inflation data
- Employment statistics
- Economic projections

**3. US Bureau of Labor Statistics**

- Employment data
- Wage growth
- Labor force participation

**4. US Energy Information Administration (EIA)**

- Oil inventory reports
- Natural gas storage
- Energy production
- Refinery utilization

---

#### Central Bank Data (3 sources)

**1. Federal Reserve**

- Interest rate decisions
- FOMC meeting minutes
- Fed speeches
- Balance sheet data

**2. European Central Bank (ECB)**

- Policy decisions
- Economic projections

**3. Bank of England**

- Rate decisions
- Monetary policy reports

---

#### Economic Calendars (2 sources)

**1. Forex Factory Calendar**

- Economic event schedule
- Impact ratings
- Consensus estimates
- Actual vs. expected

**2. Trading Economics Calendar**

- Global economic events
- Country-specific data releases
- Historical data

---

### Phase 6: Technical Analysis (T-45 to T-30 min)

#### Technical Indicator Libraries (Internal Calculation)

**1. TA-Lib (Technical Analysis Library)**

- 200+ technical indicators
- Moving averages (SMA, EMA, WMA)
- Momentum (RSI, MACD, Stochastic)
- Volatility (Bollinger Bands, ATR)
- Volume indicators
- Pattern recognition

**2. pandas-ta**

- 130+ indicators
- Custom strategies
- Overlap studies
- Momentum indicators

**3. TradingView (Optional)**

- Community indicators
- Professional charts
- Multi-timeframe analysis

---

### Phase 7: Fundamental Analysis (T-45 to T-30 min)

#### Financial Data (3 sources)

**1. Financial Modeling Prep**

- Income statements
- Balance sheets
- Cash flow statements
- Key metrics
- DCF models

**2. Alpha Vantage Fundamentals**

- Company overview
- Financial ratios
- Earnings history

**3. Intrinio**

- Historical financials
- Standardized data
- Institutional quality

---

### Phase 8: Location Data (T-40 to T-35 min)

#### Geographic Intelligence (2 sources)

**1. Google Maps API**

- Company headquarters locations
- Geocoding addresses
- Distance calculations

**2. OpenStreetMap**

- Alternative geocoding
- Point of interest data

**Internal Database**:

- Company HQ coordinates (cached)
- Exchange locations
- Regional boundaries

---

### Phase 9: AI Model Inference (T-45 to T-30 min)

#### AI/LLM APIs (3 sources)

**1. OpenAI API**

- GPT-4 Turbo for text generation
- Embeddings (ada-002) for semantic search
- Moderation API for content filtering

**2. Anthropic Claude API**

- Claude 3 Sonnet for analysis
- Long-context reasoning
- Risk assessment

**3. Cohere**

- Text embeddings
- Semantic search
- Classification

---

### Phase 10: Risk & Compliance (T-35 to T-30 min)

**1. SEC Edgar**

- Company filings
- Insider trading reports
- Regulatory actions

**2. FINRA BrokerCheck**

- Broker regulatory history
- Disciplinary actions

**3. User Compliance Database**

- Restricted securities
- Geographic restrictions
- User KYC status

---

### Phase 11: Historical Performance (T-30 to T-25 min)

**Internal Database Queries**:

- Brief's historical recommendations
- Success rates by asset class
- User portfolio performance (if tracked)
- Prediction accuracy tracking
- Model performance metrics

---

### Phase 12: Community Data (T-25 to T-20 min)

**Brief Community Database**:

- User posts and observations
- Local intelligence (parking lots, store visits)
- Community sentiment
- User predictions and their accuracy
- Geographic-specific insights

---

### Phase 13: Voice Generation (T-7 to T-5 min)

**Text-to-Speech (1 source)**:

**OpenAI TTS API** or **ElevenLabs**

- Natural voice synthesis
- Multiple voice options
- Emotion and tone control

---

### Phase 14: Email & Report (T-7 to T-3 min)

**Email Services (1 source)**:

**SendGrid** or **AWS SES**

- Email delivery
- Open/click tracking
- Bounce handling

**PDF Generation (Internal)**:

- Puppeteer (headless Chrome)
- WeasyPrint (Python)

---

## Data Source Summary by Category

### Market Data: 15 sources

- Crypto: 5 (Binance, CoinGecko, Coinbase, CryptoCompare, Glassnode)
- Forex: 3 (OANDA, Alpha Vantage, Twelve Data)
- Stocks: 5 (Yahoo, IEX, Polygon, Finnhub, FMP)
- Commodities: 2 (Quandl, Alpha Vantage)

### News & Sentiment: 12 sources

- News: 7 (NewsAPI, Benzinga, Reuters, Bloomberg, PR, FT, NZ News)
- Social: 5 (Twitter, Reddit, StockTwits, Discord, Telegram)

### Alternative Data: 13 sources

- Satellite: 2 (Planet Labs, Maxar)
- Supply Chain: 3 (MarineTraffic, FleetMon, FreightWaves)
- Consumer: 3 (SafeGraph, Placer.ai, Second Measure)
- Web Signals: 5 (LinkedIn, Indeed, App Annie, Websites, E-commerce)

### Economic Data: 9 sources

- Government: 4 (FRED, RBNZ, BLS, EIA)
- Central Banks: 3 (Fed, ECB, BoE)
- Calendars: 2 (Forex Factory, Trading Economics)

### Technical/Fundamental: 6 sources

- Technical: 3 (TA-Lib, pandas-ta, TradingView)
- Fundamental: 3 (FMP, Alpha Vantage, Intrinio)

### Location & AI: 8 sources

- Location: 2 (Google Maps, OpenStreetMap)
- AI/LLM: 3 (OpenAI, Anthropic, Cohere)
- Compliance: 2 (SEC Edgar, FINRA)
- Voice: 1 (OpenAI TTS/ElevenLabs)

### Internal Databases: 4 sources

- User data (PostgreSQL)
- Historical performance (PostgreSQL)
- Community data (MongoDB)
- Cached market data (Redis)

---

## Total Data Sources: 67+ sources interrogated

---

## API Call Volume (Per Briefing)

**Typical Briefing Generation**:

- Market data: 400-600 API calls
- News/Sentiment: 250-350 API calls
- Alternative data: 50-100 API calls
- Economic data: 20-30 API calls
- AI/LLM: 15-25 API calls
- **Total: ~750-1,100 API calls per briefing**

**Cost Per Briefing**: $0.80-1.50
**With 10,000 users**: $8,000-15,000/day in API costs

---

## Data Freshness

| Data Type         | Freshness            | Source            |
| ----------------- | -------------------- | ----------------- |
| Crypto prices     | < 1 second           | Binance WebSocket |
| Stock prices      | 15 minutes delayed\* | Yahoo Finance     |
| Stock prices      | Real-time\*          | IEX Cloud (paid)  |
| Forex             | < 1 second           | OANDA             |
| News              | < 5 minutes          | NewsAPI, Benzinga |
| Social sentiment  | < 30 minutes         | Twitter, Reddit   |
| Satellite imagery | 24 hours             | Planet Labs       |
| Economic data     | As released          | FRED, EIA         |
| Alternative data  | 24-48 hours          | Various           |

\*Real-time for Premium users

---

## Data Caching Strategy

**Cached Data** (reduces API calls):

- Historical prices: 24 hours
- Company fundamentals: 7 days
- News articles: 24 hours
- Technical indicators: 1 hour
- User preferences: Until changed
- Location data: 30 days

**Always Fresh**:

- Current prices
- Breaking news
- Social sentiment
- AI analysis
- User portfolio

---

## Redundancy & Failover

**Primary → Backup Sources**:

- Crypto: Binance → CoinGecko → Coinbase
- Stocks: IEX → Polygon → Yahoo Finance
- Forex: OANDA → Alpha Vantage → Twelve Data
- News: NewsAPI → Benzinga → Reuters

If primary source fails, automatic failover to backup within 30 seconds.

---

## Data Quality Checks

**Before Including in Brief**:

1. Cross-reference 2+ sources for price data
2. Verify news from multiple outlets
3. Filter social media bots/spam
4. Validate technical indicators
5. Sanity check AI predictions
6. Compliance screening

**Discarded Data**:

- Stale data (>24h for prices)
- Unreliable sources
- Contradictory information
- Low confidence predictions (<60%)

---

This comprehensive data interrogation is what makes Brief **institutional-grade intelligence** delivered to your phone every morning! 📊
