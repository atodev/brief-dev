# System Architecture - Brief Application

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Layer                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Flutter App  │  │   Web App    │  │  Admin Panel │      │
│  │ (iOS/Android)│  │   (React)    │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            │
                     ┌──────▼──────┐
                     │  API Gateway │
                     │   (Kong/AWS) │
                     └──────┬──────┘
                            │
┌───────────────────────────┴─────────────────────────────────┐
│                   Backend Services Layer                      │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │    User      │  │  Portfolio   │  │    Report    │      │
│  │   Service    │  │   Service    │  │   Service    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Market     │  │     AI       │  │   Briefing   │      │
│  │Data Service  │  │ Analysis Svc │  │   Service    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Research    │  │    News      │  │    Alert     │      │
│  │   Service    │  │   Service    │  │   Service    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Alternative │  │   Location   │  │  Compliance  │      │
│  │  Data Service│  │   Service    │  │   Service    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Community   │  │  AI Avatar   │  │   Moderation │      │
│  │   Service    │  │   Service    │  │   Service    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└───────────────────────────────────────────────────────────┬─┘
                            │
┌───────────────────────────┴─────────────────────────────────┐
│                    Data & AI Layer                           │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   TimeSeries │  │   ML Models  │  │   Vector DB  │      │
│  │  DB (InfluxDB│  │   (PyTorch)  │  │  (Pinecone)  │      │
│  │  /TimescaleDB│  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  PostgreSQL  │  │    Redis     │  │   MongoDB    │      │
│  │ (User/Trans) │  │   (Cache)    │  │ (Documents)  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└───────────────────────────────────────────────────────────┬─┘
                            │
┌───────────────────────────┴─────────────────────────────────┐
│                  External Data Sources                       │
│                                                               │
│  Crypto: Binance, Coinbase, CoinGecko, CryptoCompare        │
│  Forex: Alpha Vantage, OANDA, Twelve Data                   │
│  Stocks: Yahoo Finance, IEX Cloud, Polygon.io               │
│  Commodities: Quandl, CME Group APIs                         │
│  Polymarket: Polymarket API                                  │
│  News: NewsAPI, Bloomberg, Reuters, Twitter API              │
│  Alternative Data: Satellite imagery, Ship tracking,         │
│                   Parking lot analysis, Web scraping         │
└───────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. API Gateway

- **Purpose**: Single entry point for all client requests
- **Features**:
  - Rate limiting and throttling
  - Authentication/Authorization (JWT)
  - Request routing
  - Load balancing
  - API versioning
- **Technology**: Kong API Gateway or AWS API Gateway

### 2. User Service

- **Responsibilities**:
  - User registration and authentication
  - Profile management
  - Risk profile assessment
  - User location and timezone management
  - Briefing schedule preferences
  - KYC/AML verification
  - Subscription management
- **Database**: PostgreSQL with PostGIS extension (geospatial queries)
- **Auth**: OAuth 2.0 + JWT

### 3. Market Data Service

- **Responsibilities**:
  - Real-time market data ingestion
  - Historical data storage
  - Data normalization across sources
  - WebSocket streams for live updates
- **Data Sources**:
  - REST APIs for historical data
  - WebSocket connections for real-time feeds
- **Storage**: TimescaleDB/InfluxDB for time-series data
- **Cache**: Redis for frequently accessed data

### 4. AI Analysis Service

- **Responsibilities**:
  - Market sentiment analysis
  - Price prediction models
  - Pattern recognition
  - Anomaly detection
  - Risk assessment
- **Models**:
  - LSTM for time-series prediction
  - Transformer models for sentiment analysis
  - Reinforcement learning for portfolio optimization
- **Framework**: PyTorch/TensorFlow
- **Infrastructure**: GPU-enabled instances (AWS P3/P4)

### 5. Research Service

- **Responsibilities**:
  - Fundamental analysis
  - Technical indicator calculation
  - Correlation analysis
  - Market regime detection
  - Generate supporting evidence for recommendations
- **Data Processing**: Apache Spark for large-scale analysis
- **Storage**: MongoDB for research documents

### 6. News & Sentiment Service

- **Responsibilities**:
  - News aggregation and filtering
  - Social media monitoring
  - Sentiment scoring
  - Event extraction
  - Impact assessment
- **NLP**: spaCy, BERT, GPT models
- **Storage**: Elasticsearch for searchable news archive

### 7. Portfolio Service

- **Responsibilities**:
  - Manual portfolio tracking
  - Watch list management
  - Performance tracking (user-entered positions)
  - Historical recommendation tracking
  - Success rate analytics
- **Database**: PostgreSQL
- **Cache**: Redis

### 8. Report Service

- **Responsibilities**:
  - Email report generation (HTML + PDF)
  - Voice briefing script generation
  - Text-to-Speech coordination
  - Report template management
  - Historical briefing archive
  - User preference management (email time, format)
- **Technology**:
  - Email: SendGrid or AWS SES
  - PDF Generation: Puppeteer or WeasyPrint
  - Templates: Handlebars or Jinja2
- **Storage**: S3 for PDF archives and audio files
- **Database**: MongoDB for report templates

### 9. Alert Service

- **Responsibilities**:
  - Price alerts
  - Opportunity notifications
  - Risk warnings
  - Push notifications
  - Voice briefing delivery
  - Text-to-speech generation
  - Audio file storage and streaming
- **Technology**:
  - Firebase Cloud Messaging (FCM)
  - Text-to-Speech: OpenAI TTS, Google Cloud TTS, or ElevenLabs
  - Audio Storage: S3 with CloudFront CDN
- **Queue**: RabbitMQ or AWS SQS

### 10. Compliance Service

- **Responsibilities**:
  - Risk disclosure generation
  - Investment advisory disclaimers
  - User consent management
  - Content compliance review
  - Audit logging of recommendations
- **Note**: Simplified compliance since no trade execution
- **Database**: PostgreSQL (append-only audit logs)

### 10a. Alternative Data Service

- **Responsibilities**:
  - Satellite imagery analysis (oil tanks, parking lots, shipping)
  - Shadow analysis for volume estimation
  - Web scraping (job postings, store openings)
  - Ship tracking and supply chain signals
  - Foot traffic data (store visits)
  - Credit card transaction data (consumer spending)
  - App download rankings (product adoption)
  - Social media engagement metrics (brand health)
- **Technology**: Python with computer vision (OpenCV, TensorFlow)
- **Data Sources**:
  - Planet Labs, Maxar (satellite imagery)
  - MarineTraffic (ship tracking)
  - SafeGraph (foot traffic)
  - Orbital Insight (CV analysis)
- **Processing**: GPU-enabled ML models for image analysis
- **Storage**: S3 for imagery, PostgreSQL for processed insights

### 11. Briefing Service

- **Responsibilities**:
  - Orchestrate daily briefing generation
  - Coordinate data collection across all services
  - Apply location-based prioritization algorithm
  - **Generate ranked leaderboard with reasoning**
  - **Categorize opportunities by timeframe (short/long-term)**
  - **Extract key ranking factors (social, government, technical)**
  - Schedule briefing compilation jobs
  - Cache completed briefings
- **Technology**: Node.js/NestJS with Bull queue for job scheduling
- **Database**: Redis for job queue and caching
- **Timing**: Runs 30-60 minutes before user's scheduled brief time

### 12. Location Service

- **Responsibilities**:
  - Geographic proximity calculations
  - Company headquarters location data
  - Regional market identification
  - Timezone management
  - Local economic indicator tracking
  - Distance-weighted scoring
- **Database**: PostgreSQL with PostGIS extension
- **Data Sources**: Company location APIs, exchange locations
- **Algorithm**: Haversine distance formula for proximity ranking

### 13. Scheduler Service

- **Responsibilities**:
  - Manage user briefing schedules
  - Trigger briefing compilation jobs
  - Handle timezone conversions
  - Retry failed briefing generations
  - Queue management
- **Technology**: Node.js with Bull queue backed by Redis
- **Cron**: Runs continuously, checking schedules every minute

### 14. Community Service

- **Responsibilities**:
  - Manage discussion channels (by opportunity, topic, asset class)
  - Real-time chat messaging (WebSocket)
  - User posts and comments
  - Reactions and voting (upvote/downvote)
  - User profiles and reputation system
  - Thread organization and search
- **Technology**: Node.js with Socket.io for real-time
- **Database**: MongoDB for messages, Redis for online presence
- **Search**: Elasticsearch for message search

### 15. AI Avatar Service

- **Responsibilities**:
  - AI personality and avatar management
  - Natural language understanding of user questions
  - Context-aware responses in chat
  - Opportunity explanations and clarifications
  - Market education and insights
  - Sentiment analysis of community discussions
- **Technology**: Python/FastAPI with OpenAI/Anthropic APIs
- **Avatar**: Text + voice (optional) responses
- **Personality**: Professional, helpful, conversational

### 16. Moderation Service

- **Responsibilities**:
  - Content moderation (spam, abuse, inappropriate content)
  - User reporting system
  - Automated filtering (profanity, scams)
  - Community guidelines enforcement
  - User bans and warnings
- **Technology**: Python with ML-based content classification
- **Integration**: OpenAI Moderation API

## Data Flow

### 1. Market Data Ingestion Pipeline

```
External APIs → Market Data Service → Processing → TimeSeries DB
                     ↓
                  Kafka/Redis PubSub
                     ↓
            AI Analysis Service → ML Models → Predictions
```

### 2. Advisory Generation Pipeline

```
User Request → API Gateway → Research Service
                  ↓
         Fetch Market Data + News + Sentiment
                  ↓
         AI Analysis Service (Run Models)
                  ↓
         Generate Recommendation + Evidence
                  ↓
         Cache in Redis → Return to User
```

### 3. Daily Briefing Generation Pipeline (Location-Aware)

```
T-60min: Scheduler Service triggers briefing job
              ↓
T-60min: Briefing Service starts compilation
              ↓
T-59min: Fetch user location & preferences → Location Service
              ↓
T-58min: Collect market data (all asset classes) → Market Data Service
              ↓
T-55min: Fetch news & sentiment (last 24h) → News Service
              ↓
T-50min: Run AI models in parallel:
         - Price predictions (LSTM/Transformer)
         - Sentiment scoring (BERT/FinBERT)
         - Technical indicators (TA-Lib)
         - Risk assessment models
              ↓
T-40min: Location Service calculates proximity scores
         - Company HQ distances
         - Regional exchange priorities
         - Local market hours overlap
              ↓
T-35min: Research Service generates evidence
         - Fundamental analysis
         - Recent news impact
         - Historical performance
              ↓
T-25min: Briefing Service aggregates & ranks
         - Combine AI scores + location weights
         - Filter by risk profile
         - Select top N opportunities
              ↓
T-20min: Generate explanations (OpenAI/Claude)
         - Why this investment?
         - Supporting evidence
         - Risk factors
              ↓
T-15min: Compliance checks → Compliance Service
         - Regulatory restrictions
         - User eligibility
              ↓
T-10min: Final briefing assembly
         - Format for presentation
         - Generate visualizations
         - Prepare execution options
              ↓
T-7min:  Report Service generates outputs in parallel:
         ┌─────────────────┬──────────────────┐
         │                 │                  │
    Voice Script      HTML Email         PDF Report
    - Greeting        - Full analysis    - Printable
    - Weather         - Charts/graphs    - Detailed
    - Top 3-5 picks   - All 10 opps     - Archival
              ↓
T-5min:  Text-to-Speech generation
         - OpenAI TTS or ElevenLabs
         - Natural, engaging voice
         - 3-5 minute audio file
         - Store in S3 + CDN
              ↓
T-3min:  Email delivery preparation
         - Attach PDF report
         - Embed audio player link
         - Personalized subject line
         - Responsive HTML template
              ↓
T-2min:  Cache briefing → Redis
         Store: JSON + Audio URL + PDF URL
         TTL: 24 hours
              ↓
T-0:     Simultaneous delivery:
         📱 Push notification: "Your Brief is ready 🎧"
         📧 Email sent with full report + audio
         🔊 Auto-play voice briefing (if enabled)
              ↓
User Experience:
- Opens app → Voice plays automatically
- Checks email → Full detailed report with PDF
- Reviews recommendations at their own pace
```

**Total Processing Time**: 60-65 minutes
**Minimum Lead Time Required**: 1 hour before brief time

### 3. Report Generation & Delivery Flow

```
Briefing Complete → Report Service triggers
                           ↓
                   ┌───────┴────────┐
                   │                │
              Voice Gen         Email Gen
                   │                │
         ┌─────────┴────┐    ┌─────┴──────┐
         │              │    │            │
    TTS Service    Audio    HTML      PDF
    (OpenAI/11Labs) File   Template   Export
         │              │    │            │
         └──────┬───────┘    └─────┬──────┘
                │                  │
            Store in S3        Store in S3
                │                  │
         ┌──────┴──────────────────┴───────┐
         │                                  │
    Push Notification              Send Email
    "Your Brief is ready 🎧"       With PDF attachment
```

### 4. Location-Based Prioritization Algorithm

```python
def calculate_investment_score(opportunity, user_location, user_preferences):
    """
    Combines AI-predicted returns with location-based weighting
    Returns: score (0-100) and ranking_factors breakdown
    """
    # Base score from AI models (0-100)
    ai_score = opportunity.ml_prediction_score

    # Calculate geographic distance
    distance_km = calculate_haversine_distance(
        user_location,
        opportunity.company_hq_location
    )

    # Location weight decreases with distance
    # Local (0-100km): 100% weight
    # Regional (100-500km): 75% weight
    # National (500-2000km): 50% weight
    # International (2000km+): 25% weight
    if distance_km < 100:
        location_weight = 1.0
    elif distance_km < 500:
        location_weight = 0.75
    elif distance_km < 2000:
        location_weight = 0.50
    else:
        location_weight = 0.25

    # Market hours overlap (timezone consideration)
    market_overlap = calculate_market_hours_overlap(
        user_location.timezone,
        opportunity.primary_exchange.timezone
    )

    # Local economic factors
    local_economy_bonus = 0
    if opportunity.has_local_economic_impact(user_location):
        local_economy_bonus = 10

    # Final weighted score
    final_score = (
        ai_score * 0.6 +                    # 60% AI prediction
        (location_weight * 100) * 0.25 +    # 25% proximity
        (market_overlap * 100) * 0.10 +     # 10% market hours
        local_economy_bonus * 0.05          # 5% local impact
    )

    # Extract ranking factors for leaderboard display
    ranking_factors = {
        'social_sentiment': opportunity.social_sentiment_score,
        'government_impact': opportunity.regulatory_impact_score,
        'technical_strength': opportunity.technical_indicators_score,
        'fundamental_value': opportunity.fundamental_score,
        'news_momentum': opportunity.news_impact_score,
        'location_advantage': location_weight * 100,
        'timeframe': opportunity.optimal_timeframe  # 'short' or 'long'
    }

    return final_score, ranking_factors
```

## Security Architecture

### Authentication & Authorization

- **User Auth**: OAuth 2.0 + JWT tokens
- **API Keys**: Encrypted storage in HSM or AWS Secrets Manager
- **MFA**: Two-factor authentication for sensitive operations
- **Session Management**: Redis-backed sessions with timeout

### Data Security

- **Encryption at Rest**: AES-256 encryption for databases
- **Encryption in Transit**: TLS 1.3 for all communications
- **PII Protection**: Tokenization of sensitive user data
- **Key Management**: AWS KMS or HashiCorp Vault

### Network Security

- **VPC**: Isolated network for backend services
- **WAF**: Web Application Firewall for DDoS protection
- **SIEM**: Security Information and Event Management
- **Penetration Testing**: Regular security audits

## Scalability Strategy

### Horizontal Scaling

- **Stateless Services**: All services designed to scale horizontally
- **Load Balancing**: Application load balancers
- **Auto-scaling**: Based on CPU, memory, and request metrics

### Database Scaling

- **Read Replicas**: For PostgreSQL
- **Sharding**: Time-based sharding for time-series data
- **Caching**: Multi-layer caching (Redis, CDN)

### Async Processing

- **Message Queues**: RabbitMQ or AWS SQS for async tasks
- **Background Workers**: Celery for Python, Bull for Node.js
- **Batch Processing**: Apache Spark for large-scale analysis

## Monitoring & Observability

### Logging

- **Centralized Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Structured Logging**: JSON format with correlation IDs
- **Log Levels**: DEBUG, INFO, WARN, ERROR, FATAL

### Metrics

- **Time-Series Metrics**: Prometheus + Grafana
- **APM**: Application Performance Monitoring (New Relic, Datadog)
- **Custom Dashboards**: Business metrics and KPIs

### Tracing

- **Distributed Tracing**: Jaeger or AWS X-Ray
- **Request Tracking**: End-to-end transaction visibility

### Alerting

- **PagerDuty**: For critical issues
- **Slack Integration**: For team notifications
- **SLA Monitoring**: Uptime and performance SLAs

## Disaster Recovery

### Backup Strategy

- **Database Backups**: Daily full backups, hourly incremental
- **Point-in-Time Recovery**: For PostgreSQL
- **Geographic Redundancy**: Multi-region deployment

### Business Continuity

- **RTO**: Recovery Time Objective < 1 hour
- **RPO**: Recovery Point Objective < 5 minutes
- **Failover**: Automated failover to standby region
- **DR Drills**: Quarterly disaster recovery testing
