# Data Sources & API Reference

This document provides detailed information about all external data sources and APIs needed for the Brief application.

---

## Cryptocurrency Data

### 1. CoinGecko API

- **Website**: https://www.coingecko.com/en/api
- **Purpose**: Aggregated cryptocurrency data
- **Pricing**: Free tier available, Pro from $129/month
- **Features**:
  - 13,000+ cryptocurrencies
  - Historical data
  - Market data (price, volume, market cap)
  - DEX data
  - NFT data
- **Rate Limits**: 10-50 calls/minute (free tier)
- **Best For**: General crypto market overview

### 2. Binance API

- **Website**: https://binance-docs.github.io/apidocs/
- **Purpose**: Real-time crypto trading data
- **Pricing**: Free (requires account)
- **Features**:
  - Real-time orderbook
  - Trade history
  - Kline/candlestick data
  - WebSocket streams
  - Trading execution
- **Rate Limits**: 1200 requests/minute
- **Best For**: High-frequency crypto data, trading

### 3. Coinbase Advanced Trade API

- **Website**: https://docs.cloud.coinbase.com/
- **Purpose**: Crypto trading and data
- **Pricing**: Free (requires account)
- **Features**:
  - Market data
  - Trading
  - Portfolio management
  - Institutional-grade
- **Best For**: US-based crypto trading

### 4. CryptoCompare

- **Website**: https://www.cryptocompare.com/api
- **Purpose**: Historical and real-time crypto data
- **Pricing**: Free tier, Pro from $30/month
- **Features**:
  - Historical OHLCV
  - Social data
  - News aggregation
  - Multiple exchanges
- **Best For**: Historical analysis

---

## Forex Data

### 1. Alpha Vantage

- **Website**: https://www.alphavantage.co/
- **Purpose**: Free stock, forex, and crypto API
- **Pricing**: Free (500 calls/day), Premium from $49.99/month
- **Features**:
  - Intraday forex
  - Daily/weekly/monthly data
  - Technical indicators
  - Multiple asset classes
- **Rate Limits**: 5 calls/minute (free)
- **Best For**: Getting started, mixed asset classes

### 2. OANDA API

- **Website**: https://developer.oanda.com/
- **Purpose**: Professional forex data and trading
- **Pricing**: Free for data, trading requires funded account
- **Features**:
  - Real-time streaming rates
  - Historical data
  - 120+ currency pairs
  - Trading execution
- **Rate Limits**: Varies by account type
- **Best For**: Serious forex trading

### 3. Twelve Data

- **Website**: https://twelvedata.com/
- **Purpose**: Financial data API
- **Pricing**: Free tier (800 calls/day), Basic $9/month
- **Features**:
  - Forex, stocks, crypto
  - Technical indicators
  - WebSocket support
  - High frequency data
- **Rate Limits**: 8 calls/minute (free)
- **Best For**: Multi-asset API

### 4. Fixer.io

- **Website**: https://fixer.io/
- **Purpose**: Currency exchange rates
- **Pricing**: Free tier (100 calls/month), Basic $10/month
- **Features**:
  - 170+ currencies
  - Historical data since 1999
  - Currency conversion
- **Best For**: Simple currency conversions

---

## Stock Market Data

### 1. Yahoo Finance (yfinance)

- **Library**: https://github.com/ranaroussi/yfinance
- **Purpose**: Free stock market data
- **Pricing**: Free (unofficial API)
- **Features**:
  - Global stocks
  - Historical data
  - Options data
  - Dividends, splits
  - Company info
- **Rate Limits**: Unclear (use responsibly)
- **Best For**: Research, backtesting
- **Note**: Unofficial, could break

### 2. IEX Cloud

- **Website**: https://iexcloud.io/
- **Purpose**: US stock market data
- **Pricing**: Free tier (50,000 messages/month), Launch $9/month
- **Features**:
  - Real-time quotes
  - Historical data
  - Company fundamentals
  - News
  - Alternative data
- **Rate Limits**: Based on message credits
- **Best For**: US stocks, reliable API

### 3. Polygon.io

- **Website**: https://polygon.io/
- **Purpose**: Comprehensive market data
- **Pricing**: Starter $29/month (live data), Free tier (delayed)
- **Features**:
  - Stocks, options, crypto, forex
  - Real-time and historical
  - WebSocket streams
  - Reference data
- **Rate Limits**: 5 calls/minute (free)
- **Best For**: Professional applications

### 4. Finnhub

- **Website**: https://finnhub.io/
- **Purpose**: Real-time financial data
- **Pricing**: Free tier (60 calls/minute), Basic $39.99/month
- **Features**:
  - Stock quotes
  - Company news
  - Earnings
  - Financial statements
  - WebSocket
- **Best For**: News and fundamentals

### 5. Financial Modeling Prep

- **Website**: https://site.financialmodelingprep.com/
- **Purpose**: Financial statements and ratios
- **Pricing**: Free tier (250 calls/day), Starter $14/month
- **Features**:
  - Company financials
  - Ratios and metrics
  - Historical data
  - 15+ years history
- **Best For**: Fundamental analysis

---

## Commodities Data

### 1. Quandl (Nasdaq Data Link)

- **Website**: https://data.nasdaq.com/
- **Purpose**: Alternative and financial data
- **Pricing**: Free tier limited, Premium varies
- **Features**:
  - Commodities prices
  - Economic indicators
  - Futures data
  - Historical data
- **Best For**: Comprehensive commodities

### 2. CME Group API

- **Website**: https://www.cmegroup.com/market-data/
- **Purpose**: Futures and options data
- **Pricing**: Varies (professional data)
- **Features**:
  - Real-time futures
  - Options data
  - Settlement prices
  - Volume and open interest
- **Best For**: Professional commodities trading

### 3. Alpha Vantage (Commodities)

- **Features**:
  - WTI and Brent crude oil
  - Natural gas
  - Copper
  - Aluminum
  - Wheat, corn, cotton, sugar, coffee
- **Best For**: Basic commodities tracking

---

## Prediction Markets

### 1. Polymarket API

- **Website**: https://docs.polymarket.com/
- **Purpose**: Decentralized prediction market
- **Pricing**: Free (blockchain-based)
- **Features**:
  - Market odds
  - Trading volume
  - Event outcomes
  - Historical data
- **Best For**: Event-driven trading

### 2. Augur

- **Website**: https://augur.net/
- **Purpose**: Decentralized prediction markets
- **Pricing**: Free (requires crypto wallet)
- **Features**:
  - User-created markets
  - Odds and volume
  - Blockchain-based
- **Best For**: Alternative predictions

### 3. PredictIt

- **Website**: https://www.predictit.org/
- **Purpose**: Political prediction markets
- **Pricing**: Free to access data
- **Features**:
  - Political events
  - Market prices
  - Historical data
- **Best For**: Political events

---

## News & Sentiment Data

### 1. NewsAPI

- **Website**: https://newsapi.org/
- **Purpose**: News aggregation
- **Pricing**: Free tier (100 calls/day), Pro from $449/month
- **Features**:
  - 80,000+ news sources
  - Search and filtering
  - Historical articles
  - Multiple languages
- **Rate Limits**: 100 requests/day (free)
- **Best For**: General news aggregation

### 2. Bloomberg API (Terminal)

- **Website**: https://www.bloomberg.com/professional/support/api-library/
- **Purpose**: Professional financial news
- **Pricing**: Requires Bloomberg Terminal (~$24,000/year)
- **Features**:
  - Real-time news
  - Company events
  - Analyst reports
  - Market data
- **Best For**: Institutional use only

### 3. Benzinga News API

- **Website**: https://www.benzinga.com/apis
- **Purpose**: Financial news and events
- **Pricing**: Starts at $150/month
- **Features**:
  - Real-time news
  - Earnings calendars
  - Analyst ratings
  - Stock-specific news
- **Best For**: Stock news

### 4. Twitter API

- **Website**: https://developer.twitter.com/
- **Purpose**: Social media sentiment
- **Pricing**: Free tier available, Basic $100/month
- **Features**:
  - Tweet search
  - Streaming
  - User metrics
  - Historical data
- **Rate Limits**: Varies by tier
- **Best For**: Real-time sentiment

### 5. Reddit API

- **Website**: https://www.reddit.com/dev/api/
- **Purpose**: Community sentiment
- **Pricing**: Free
- **Features**:
  - Subreddit posts
  - Comments
  - Voting data
  - Real-time streams
- **Rate Limits**: 60 requests/minute
- **Best For**: Retail investor sentiment

---

## Alternative Data

### 1. Quiver Quantitative

- **Website**: https://www.quiverquant.com/
- **Purpose**: Alternative data aggregation
- **Pricing**: Free tier, Premium $30/month
- **Features**:
  - Insider trading
  - Lobbying data
  - Congress trading
  - Corporate flights
- **Best For**: Alternative signals

### 2. Unusual Whales

- **Website**: https://unusualwhales.com/
- **Purpose**: Options flow and market data
- **Pricing**: Premium subscription required
- **Features**:
  - Unusual options activity
  - Market flows
  - Dark pool data
- **Best For**: Options trading signals

---

## Economic Data

### 1. Federal Reserve Economic Data (FRED)

- **Website**: https://fred.stlouisfed.org/
- **Purpose**: US economic indicators
- **Pricing**: Free
- **Features**:
  - 800,000+ time series
  - GDP, inflation, employment
  - Historical data
  - API access
- **Best For**: Macroeconomic analysis

### 2. World Bank API

- **Website**: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589
- **Purpose**: Global economic data
- **Pricing**: Free
- **Features**:
  - Country statistics
  - Development indicators
  - Historical data
- **Best For**: International economics

---

## AI/LLM APIs

### 1. OpenAI API

- **Website**: https://platform.openai.com/
- **Purpose**: AI text generation and analysis
- **Pricing**: Pay-per-use, ~$0.01-0.06 per 1K tokens
- **Models**:
  - GPT-4 Turbo
  - GPT-3.5 Turbo
  - Embeddings (ada-002)
- **Best For**: Text generation, summarization, analysis

### 2. Anthropic Claude API

- **Website**: https://www.anthropic.com/api
- **Purpose**: AI assistant and analysis
- **Pricing**: Pay-per-use
- **Models**:
  - Claude 3 Opus
  - Claude 3 Sonnet
- **Best For**: Long-context analysis, reasoning

### 3. Cohere

- **Website**: https://cohere.ai/
- **Purpose**: NLP and embeddings
- **Pricing**: Free tier, Production pricing varies
- **Features**:
  - Text generation
  - Embeddings
  - Classification
- **Best For**: Embeddings and classification

---

## Technical Analysis Libraries

### 1. TA-Lib

- **Website**: https://ta-lib.org/
- **Type**: Python library
- **Pricing**: Free (open source)
- **Features**:
  - 200+ technical indicators
  - Pattern recognition
  - Math functions
- **Installation**: `pip install TA-Lib`

### 2. pandas-ta

- **Website**: https://github.com/twopirllc/pandas-ta
- **Type**: Python library
- **Pricing**: Free (open source)
- **Features**:
  - 130+ indicators
  - Pandas integration
  - Custom strategies
- **Installation**: `pip install pandas-ta`

---

## Backtesting & Trading

### 1. Backtrader

- **Website**: https://www.backtrader.com/
- **Type**: Python library
- **Pricing**: Free (open source)
- **Features**:
  - Strategy backtesting
  - Portfolio analysis
  - Multiple data feeds
- **Installation**: `pip install backtrader`

### 2. Alpaca API

- **Website**: https://alpaca.markets/
- **Purpose**: Commission-free stock trading API
- **Pricing**: Free (no commissions)
- **Features**:
  - Paper trading
  - Live trading (US stocks)
  - Market data
  - Real-time streams
- **Best For**: US stock trading automation

---

## API Integration Strategy

### Development Phase

- Use free tiers and unofficial APIs (yfinance)
- Focus on 1-2 sources per asset class
- Implement caching aggressively
- Mock data for testing

### Production Phase

- Migrate to paid, reliable APIs
- Implement redundancy (multiple sources)
- Set up monitoring for API health
- Negotiate bulk pricing
- Implement rate limiting and queueing

### Cost Management

- Cache frequently requested data (Redis)
- Batch API calls where possible
- Use webhooks instead of polling
- Implement data retention policies
- Monitor and optimize API usage

---

## Recommended Initial Setup (MVP)

### Minimum Viable Data Sources

1. **Crypto**: CoinGecko (free)
2. **Forex**: Alpha Vantage (free)
3. **Stocks**: yfinance (free)
4. **News**: NewsAPI (free tier)
5. **AI**: OpenAI API (pay-as-you-go)

**Estimated Monthly Cost**: $50-200

### Production Data Sources

1. **Crypto**: Binance + CoinGecko Pro
2. **Forex**: OANDA + Alpha Vantage Premium
3. **Stocks**: Polygon.io + IEX Cloud
4. **Commodities**: Quandl
5. **Polymarket**: Polymarket API
6. **News**: NewsAPI Pro + Benzinga
7. **AI**: OpenAI + Anthropic

**Estimated Monthly Cost**: $500-2000

---

## Data Quality & Reliability

### Best Practices

1. **Multiple Sources**: Cross-reference data from 2+ sources
2. **Data Validation**: Implement anomaly detection
3. **Monitoring**: Track API uptime and data freshness
4. **Fallbacks**: Automatic failover to backup sources
5. **Caching**: Reduce API calls and improve response time
6. **Testing**: Regular data quality audits

### Data Freshness Requirements

- **Real-time**: Crypto, forex (< 1 second delay)
- **Near real-time**: Stocks (< 15 minutes)
- **Daily**: Commodities, fundamentals
- **News**: Within 5 minutes of publication
- **ML Models**: Retrain weekly/monthly

---

## Legal & Compliance Considerations

### Data Licensing

- Read and comply with all API Terms of Service
- Some APIs prohibit redistribution of data
- Commercial use may require separate licensing
- Be aware of exchange data fees

### Financial Regulations

- May need licenses to provide certain data
- Market data regulations (e.g., Regulation NMS for US stocks)
- Real-time data often requires exchange fees
- Delayed data (15+ minutes) usually free

### Data Privacy

- Comply with GDPR for user data
- Don't mix user PII with market data
- Secure API keys properly
- Implement data retention policies
