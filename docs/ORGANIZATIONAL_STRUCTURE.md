# Brief: Organizational Structure & Roles

**Company**: Brief Limited  
**Type**: AI Financial Intelligence Platform  
**Stage**: Pre-Seed / MVP Development  
**Headquarters**: Auckland, New Zealand  
**Employee Count**: 0 (founding team) → 180 (by Year 5)

---

## Mission & Vision

### Mission Statement

**To democratize financial intelligence by making institutional-grade market analysis accessible to every investor, regardless of wealth or location.**

We exist to level the playing field between retail and institutional investors. By combining cutting-edge AI, alternative data sources, and location-based intelligence, we deliver actionable insights that were previously only available to Wall Street professionals—at 99% less cost.

### Vision Statement

**To become the world's most trusted source of financial intelligence, serving 10 million investors across 100 cities by 2030.**

We envision a future where every investor—from Auckland to Singapore to New York—starts their day with a personalized Brief that helps them make smarter financial decisions. Where information asymmetry is eliminated, and success is determined by insight, not insider access.

### How We Achieve This

1. **AI-First Approach**: Leverage GPT-4, FinBERT, and LSTM models to analyze markets 24/7
2. **Alternative Data**: Satellite imagery, foot traffic, credit card data—insights institutions pay millions for
3. **Location Intelligence**: First-mover advantage in 50+ cities, starting with Auckland
4. **Transparency**: 87% accuracy tracking, clear disclaimers, "observations not advice" positioning
5. **Community**: Connect investors in each city, democratize knowledge sharing
6. **Affordability**: $10-300/month vs. Bloomberg's $24,000/year

---

## Table of Contents

1. [Organizational Chart](#organizational-chart)
2. [Executive Team](#executive-team)
3. [Engineering Department](#engineering-department)
4. [Product & Design Department](#product--design-department)
5. [Data & AI Department](#data--ai-department)
6. [Marketing & Growth Department](#marketing--growth-department)
7. [Sales & Partnerships Department](#sales--partnerships-department)
8. [Customer Success Department](#customer-success-department)
9. [Operations & Finance Department](#operations--finance-department)
10. [Legal & Compliance Department](#legal--compliance-department)
11. [Hiring Timeline](#hiring-timeline)
12. [Compensation Structure](#compensation-structure)
13. [Company Culture & Values](#company-culture--values)

---

## Organizational Chart

### Phase 1: Founding Team (Months 0-3) - 3 People

```
                    CEO/Founder
                         |
            +-----------+------------+
            |                        |
        CTO/Co-Founder          CPO/Co-Founder
```

### Phase 2: MVP Team (Months 1-6) - 10 People

```
                         CEO
                          |
         +----------------+------------------+
         |                |                  |
        CTO              CPO            Head of Growth
         |                |                  |
    +----+----+      +----+----+        Marketing Manager
    |         |      |         |
Engineers   ML Eng  Designer  PM
(3)         (1)     (1)       (1)
```

### Phase 3: Launch Team (Months 7-18) - 40 People

```
                              CEO
                               |
        +----------------------+------------------------+
        |                      |                        |
       CTO                    CPO                   Head of Growth
        |                      |                        |
   +----+----+           +-----+-----+            +-----+-----+
   |    |    |           |     |     |            |     |     |
Backend Mobile Infra  Product Design UX      Marketing Sales CS
(8)    (3)   (2)      (2)    (2)   (1)        (3)    (2)  (3)

                               |
                               +
                        Head of Data/AI
                               |
                         +-----+-----+
                         |           |
                    Data Sci    ML Eng
                      (2)        (2)
```

### Phase 4: Scale Team (Months 19-36) - 100 People

```
                                    CEO
                                     |
            +------------------------+---------------------------+
            |                        |                           |
      C-Suite (CTO, CPO, CMO)    VP Data/AI            VP Sales & Partnerships
            |                        |                           |
    +-------+-------+          +-----+-----+              +------+------+
    |       |       |          |           |              |      |      |
 Backend  Mobile  Infra   Data Sci    ML Eng        Enterprise Brokers Community
  (15)    (6)     (5)       (5)        (5)            (5)      (3)     (3)

            |                        |                           |
            +                        +                           +
      Product & Design          Marketing & Growth        Customer Success
            |                        |                           |
      +-----+-----+            +-----+-----+              +------+------+
      |     |     |            |     |     |              |      |      |
     PM  Design  UX        Content  PR  Perf.Mkt      Support  Onboard  QA
    (4)   (4)   (2)          (3)   (2)   (5)           (8)     (3)     (2)
```

---

## Executive Team

### 1. Chief Executive Officer (CEO)

**Reports To**: Board of Directors  
**Direct Reports**: CTO, CPO, CMO, VP Data/AI, VP Sales, CFO, General Counsel

**Responsibilities**:

- Set company vision, mission, and strategic direction
- Lead fundraising efforts (Seed, Series A, Series B)
- Build relationships with key investors, advisors, board members
- Represent Brief publicly (media, conferences, podcasts)
- Make final decisions on product direction, hiring, partnerships
- Ensure company execution against OKRs (Objectives & Key Results)
- Build and maintain company culture
- Approve budgets and major expenditures (>$50K)

**Key Duties**:

- **Fundraising** (30%): Pitch decks, investor meetings, due diligence, closing rounds
- **Strategy** (25%): OKR setting, strategic planning, market positioning
- **Partnerships** (20%): Data providers (Planet Labs), brokers (Hatch, Stake), regulators
- **People** (15%): Executive hiring, culture building, all-hands meetings
- **Product** (10%): Final approval on roadmap, feature prioritization

**Success Metrics**:

- Capital raised ($2M seed, $10M Series A, $30M Series B on schedule)
- User growth (10K → 50K → 150K on roadmap)
- Revenue growth (MRR: $122K → $735K → $2.42M)
- Team growth (10 → 40 → 100 quality hires)
- Product-market fit (NPS >50, retention >80%)

**Skills Required**:

- Fundraising & investor relations
- Strategic thinking & vision
- Executive leadership
- Public speaking & media
- Financial acumen

**Compensation** (Year 1):

- Salary: $120K-150K
- Equity: 20-30% (founder shares)
- Bonus: 10% of salary (tied to fundraising milestones)

---

### 2. Chief Technology Officer (CTO)

**Reports To**: CEO  
**Direct Reports**: VP Engineering (Backend), VP Engineering (Mobile), Head of Infrastructure, Head of Security

**Responsibilities**:

- Own all technical architecture and infrastructure decisions
- Build and lead engineering team (3 → 50+ engineers over 3 years)
- Ensure system scalability (100 users → 500K users)
- Maintain 99.9% uptime SLA
- Set engineering standards, code quality, CI/CD processes
- Evaluate and integrate new technologies (AI models, databases, cloud services)
- Manage technical debt and refactoring priorities
- Ensure security and compliance (SOC 2, GDPR, data encryption)
- Partner with CPO on technical feasibility of product roadmap

**Key Duties**:

- **Architecture** (30%): System design, microservices, databases, APIs
- **Team Building** (25%): Hiring engineers, code reviews, mentorship, 1-on-1s
- **Infrastructure** (20%): AWS, Kubernetes, CI/CD, monitoring, cost optimization
- **Security** (15%): Penetration testing, compliance, data protection
- **Innovation** (10%): Evaluate new AI models, data sources, tech stack improvements

**Success Metrics**:

- System uptime: 99.9%+
- Page load time: <2 seconds
- API response time: <200ms (p95)
- Briefing generation time: <60 seconds (T-60 to T-0)
- Cost per user: <$2/month
- Engineering team velocity: 12+ features shipped per quarter
- Zero security breaches
- SOC 2 certification achieved

**Skills Required**:

- System architecture (microservices, distributed systems)
- Cloud infrastructure (AWS, Kubernetes, Terraform)
- Backend development (Node.js, Python, databases)
- Team leadership (hiring, mentoring, performance management)
- Security & compliance (SOC 2, encryption, GDPR)

**Compensation** (Year 1):

- Salary: $150K-180K
- Equity: 5-10% (co-founder or early employee)
- Bonus: 15% of salary (tied to uptime, velocity metrics)

---

### 3. Chief Product Officer (CPO)

**Reports To**: CEO  
**Direct Reports**: VP Product, Head of Design, Head of User Research, Product Managers (4)

**Responsibilities**:

- Own product vision, strategy, and roadmap
- Conduct user research and validate product-market fit
- Prioritize features based on user needs, business value, technical feasibility
- Define success metrics for every feature (adoption, engagement, retention)
- Collaborate with CTO on technical feasibility
- Ensure exceptional user experience (mobile app, email, voice)
- Analyze product analytics and iterate based on data
- Lead product team (PMs, designers, researchers)

**Key Duties**:

- **Product Strategy** (30%): Roadmap planning, feature prioritization, OKRs
- **User Research** (25%): Interviews, surveys, usability testing, feedback analysis
- **Product Management** (20%): Feature specs, user stories, acceptance criteria
- **Analytics** (15%): Mixpanel dashboards, A/B testing, cohort analysis
- **Design Collaboration** (10%): UI/UX reviews, design system, prototypes

**Success Metrics**:

- User engagement: 40% DAU/MAU (daily active / monthly active)
- Feature adoption: 60%+ of users use new features within 30 days
- Net Promoter Score (NPS): 50+
- User retention: 80% (30-day), 60% (90-day)
- Time to value: <5 minutes (signup to first briefing)
- App store rating: 4.5+ stars
- Product velocity: 12+ features shipped per quarter

**Skills Required**:

- Product management (roadmapping, prioritization, PRDs)
- User research (interviews, surveys, usability testing)
- Data analysis (SQL, Mixpanel, A/B testing)
- UX/UI principles (wireframing, prototyping)
- Communication (cross-functional alignment)

**Compensation** (Year 1):

- Salary: $140K-170K
- Equity: 3-8% (co-founder or early employee)
- Bonus: 15% of salary (tied to NPS, retention metrics)

---

### 4. Chief Marketing Officer (CMO)

**Hired**: Month 12-18  
**Reports To**: CEO  
**Direct Reports**: VP Marketing, Head of Growth, Head of Content, Head of PR

**Responsibilities**:

- Build and execute marketing strategy (brand, performance, content)
- Drive user acquisition (CAC <$25, LTV/CAC >10x)
- Manage marketing budget ($300K → $3M over 3 years)
- Build brand awareness and thought leadership
- Develop partnerships (brokers, influencers, media)
- Lead marketing team (10+ people by Year 2)
- Analyze marketing channels and optimize ROI

**Key Duties**:

- **Growth Marketing** (35%): Facebook/Google ads, SEO, referral programs
- **Brand** (25%): Positioning, messaging, PR, thought leadership
- **Content** (20%): Blog posts, videos, podcasts, social media
- **Analytics** (15%): CAC, LTV, conversion funnels, attribution
- **Partnerships** (5%): Co-marketing, influencers, affiliate programs

**Success Metrics**:

- User acquisition: 10K (Year 1) → 50K (Year 2) → 150K (Year 3)
- CAC: <$25 blended
- LTV/CAC: >10x
- Paid conversion rate: 40% → 70%
- Brand awareness: 80% in target markets (surveys)
- Media mentions: 50+ per month
- Marketing ROI: $3+ revenue per $1 spent

**Skills Required**:

- Performance marketing (Facebook, Google, analytics)
- Brand strategy (positioning, messaging, storytelling)
- Content marketing (SEO, blog, video, social)
- Data-driven decision making (attribution, cohort analysis)
- Team leadership (hiring, managing agencies)

**Compensation** (Year 2):

- Salary: $160K-200K
- Equity: 0.5-2%
- Bonus: 20% of salary (tied to CAC, user growth)

---

### 5. VP of Data & AI

**Hired**: Month 3-6  
**Reports To**: CEO (initially), then CTO (after scaling)  
**Direct Reports**: Data Scientists (5), ML Engineers (5), Data Engineers (3)

**Responsibilities**:

- Build and train AI models (price prediction, sentiment analysis, opportunity ranking)
- Own alternative data pipeline (satellite, foot traffic, credit card data)
- Ensure 87%+ prediction accuracy on A-grade signals
- Develop personalization engine (user-specific models)
- Manage data partnerships (Planet Labs, SafeGraph, Second Measure)
- Optimize AI costs (GPT-4 → self-hosted models where possible)
- Build data infrastructure (data lake, feature store, model registry)

**Key Duties**:

- **Model Development** (40%): Train LSTM, FinBERT, Prophet models
- **Data Pipelines** (25%): ETL, data quality, alternative data integration
- **Experimentation** (20%): A/B testing, model evaluation, hyperparameter tuning
- **Cost Optimization** (10%): Self-host models, cache predictions, batch processing
- **Team Leadership** (5%): Hiring, code reviews, research

**Success Metrics**:

- Prediction accuracy: 87%+ (A-grade signals)
- Model latency: <5 seconds (inference time)
- AI cost per briefing: <$0.50
- Alternative data integrations: 5+ sources (satellite, foot traffic, credit cards)
- Data freshness: <24 hours for alternative data
- Model improvements: +2% accuracy per quarter

**Skills Required**:

- Machine learning (PyTorch, TensorFlow, scikit-learn)
- NLP (transformers, sentiment analysis, FinBERT)
- Time-series forecasting (LSTM, Prophet, ARIMA)
- Data engineering (Spark, Airflow, data lakes)
- Cloud ML infrastructure (AWS SageMaker, GPU optimization)

**Compensation** (Year 1):

- Salary: $180K-220K
- Equity: 1-3%
- Bonus: 20% of salary (tied to accuracy, cost metrics)

---

### 6. VP of Sales & Partnerships

**Hired**: Month 12-18  
**Reports To**: CEO  
**Direct Reports**: Enterprise Sales (5), Broker Partnerships (3), Community Managers (3)

**Responsibilities**:

- Build enterprise sales pipeline (financial advisors, institutions)
- Negotiate broker partnerships (30+ partners: Hatch, Stake, Robinhood, etc.)
- Manage broker affiliate revenue ($300K → $13.65M over 3 years)
- Develop data partnerships (Planet Labs, SafeGraph, Second Measure)
- Lead community engagement and growth
- Build sales playbook and training materials

**Key Duties**:

- **Enterprise Sales** (35%): Outreach, demos, closing deals
- **Broker Partnerships** (30%): Contract negotiations, integrations, revenue tracking
- **Data Partnerships** (20%): Negotiate exclusive deals, pricing, SLAs
- **Community** (10%): Engagement, moderation, user-generated content
- **Reporting** (5%): Sales metrics, pipeline health, forecasting

**Success Metrics**:

- Enterprise deals: 20+ by Year 2 ($5K-25K ACV each)
- Broker partnerships: 30+ live integrations
- Broker affiliate revenue: $300K (Year 1) → $13.65M (Year 3)
- Data partnership savings: 20% discount via multi-year contracts
- Community engagement: 40% DAU/MAU, 500+ posts per day

**Skills Required**:

- B2B sales (enterprise, SaaS)
- Partnership negotiation (contracts, revenue share)
- Community management (engagement, moderation)
- CRM tools (Salesforce, HubSpot)
- Financial services domain knowledge

**Compensation** (Year 2):

- Salary: $120K-150K
- Equity: 0.5-1.5%
- Bonus: 30% of salary + commission (tied to revenue, partnerships)

---

### 7. Chief Financial Officer (CFO)

**Hired**: Month 18-24  
**Reports To**: CEO  
**Direct Reports**: Finance Manager, Accounting, FP&A Analyst

**Responsibilities**:

- Manage all financial operations (budgeting, forecasting, cash flow)
- Lead fundraising efforts (financial models, data room, investor relations)
- Ensure compliance with financial regulations (audit, tax, reporting)
- Optimize unit economics (CAC, LTV, gross margin)
- Manage vendor relationships and negotiate contracts
- Prepare for IPO or acquisition (financial statements, due diligence)

**Key Duties**:

- **Financial Planning** (30%): Budgets, forecasts, scenario modeling
- **Fundraising** (25%): Financial models, investor decks, due diligence
- **Operations** (20%): Cash management, payroll, AP/AR
- **Compliance** (15%): Audits, tax filings, financial reporting
- **Analytics** (10%): Unit economics, margin analysis, cost optimization

**Success Metrics**:

- Cash runway: Always >12 months
- Gross margin: 85%+ at scale
- Burn rate: On budget (±5%)
- Fundraising: Successful rounds on schedule
- Audit: Clean audit reports (zero material findings)
- Cost optimization: 10% reduction in infrastructure costs annually

**Skills Required**:

- Financial modeling (Excel, scenario analysis)
- Fundraising & investor relations
- Accounting & compliance (GAAP, audit, tax)
- SaaS metrics (CAC, LTV, MRR, churn)
- Strategic finance (M&A, IPO preparation)

**Compensation** (Year 2):

- Salary: $180K-220K
- Equity: 0.5-2%
- Bonus: 15% of salary (tied to fundraising, financial targets)

---

### 8. General Counsel (GC) / Head of Legal & Compliance

**Hired**: Month 12-18 (initially part-time consultant, then full-time)  
**Reports To**: CEO  
**Direct Reports**: Compliance Manager, Regulatory Analyst

**Responsibilities**:

- Ensure regulatory compliance (securities law, financial services)
- Manage "observations not advice" positioning to avoid RIA licensing
- Review all user-facing content (disclaimers, Terms of Service, Privacy Policy)
- Negotiate contracts (data providers, brokers, vendors)
- Manage licenses in 5+ countries (NZ, AU, US, UK, SG)
- Handle legal disputes, intellectual property, employment law
- Prepare for SOC 2 Type II certification

**Key Duties**:

- **Regulatory Compliance** (40%): Securities law, GDPR, CCPA, data protection
- **Contracts** (25%): Vendor agreements, data partnerships, broker contracts
- **Risk Management** (20%): Terms of Service, disclaimers, liability protection
- **Licensing** (10%): Apply for licenses in new jurisdictions
- **Litigation** (5%): Handle disputes, employment issues

**Success Metrics**:

- Zero regulatory violations
- SOC 2 Type II certification achieved
- Licenses obtained: 5+ countries
- Contract review turnaround: <5 business days
- Legal costs: <$500K/year
- Risk mitigation: All content reviewed and compliant

**Skills Required**:

- Securities law (financial services, investment advisors)
- Regulatory compliance (GDPR, CCPA, data protection)
- Contract negotiation (SaaS, data partnerships)
- Corporate law (fundraising, M&A, IPO)
- Risk management (disclaimers, liability, insurance)

**Compensation** (Year 2):

- Salary: $150K-200K
- Equity: 0.25-1%
- Bonus: 10% of salary

---

## Engineering Department

### VP of Engineering (Backend)

**Hired**: Month 6-9  
**Reports To**: CTO  
**Direct Reports**: Backend Engineers (15), DevOps Engineers (3)

**Responsibilities**:

- Lead backend development (16 microservices: User, Market Data, AI Analysis, Briefing, Location, etc.)
- Ensure system scalability (10K → 500K users)
- Manage technical debt and code quality
- Implement best practices (code reviews, testing, documentation)
- Optimize database performance (PostgreSQL, TimescaleDB, MongoDB, Redis)

**Key Duties**:

- **Development** (40%): Feature development, code reviews, architecture decisions
- **Team Leadership** (25%): Hiring, 1-on-1s, performance reviews, mentorship
- **Operations** (20%): Incident response, on-call rotation, monitoring
- **Planning** (15%): Sprint planning, backlog grooming, technical roadmap

**Success Metrics**:

- API uptime: 99.9%+
- API response time: <200ms (p95)
- Code coverage: >80%
- Technical debt: <20% of sprint capacity
- Feature velocity: 12+ features per quarter
- Zero critical bugs in production

**Compensation** (Year 1):

- Salary: $140K-170K
- Equity: 0.5-1.5%
- Bonus: 15% (tied to uptime, velocity)

---

### Senior Backend Engineer

**Hired**: Months 1-3 (first 3 hires)  
**Reports To**: VP Engineering (Backend) or CTO initially  
**Direct Reports**: None (individual contributor)

**Responsibilities**:

- Build and maintain microservices (NestJS/Node.js, FastAPI/Python)
- Design RESTful APIs and GraphQL endpoints
- Optimize database queries and data models
- Implement caching strategies (Redis)
- Write unit tests and integration tests (80%+ coverage)
- Participate in on-call rotation (incident response)

**Key Duties**:

- **Feature Development** (60%): Build new features, fix bugs
- **Code Review** (15%): Review PRs from team members
- **Operations** (15%): Monitor logs, respond to incidents
- **Documentation** (10%): API docs, architecture diagrams

**Success Metrics**:

- Features delivered on time: 95%+
- Code quality: Zero critical bugs introduced
- PR review turnaround: <24 hours
- On-call response time: <15 minutes

**Skills Required**:

- Backend development (Node.js or Python)
- Databases (PostgreSQL, MongoDB, Redis)
- RESTful APIs and microservices
- Testing (Jest, pytest)
- Cloud platforms (AWS, Docker, Kubernetes)

**Compensation** (Year 1):

- Salary: $100K-130K
- Equity: 0.1-0.5%
- Bonus: 10%

---

### Mobile Engineer (Flutter)

**Hired**: Months 3-6 (2-3 hires)  
**Reports To**: VP Engineering (Mobile) or CTO initially  
**Direct Reports**: None

**Responsibilities**:

- Build iOS and Android apps using Flutter
- Implement push notifications (portfolio alerts)
- Optimize app performance and battery usage
- Integrate with backend APIs (REST, GraphQL, WebSocket)
- Submit apps to App Store and Google Play
- Fix bugs and respond to user feedback

**Key Duties**:

- **App Development** (70%): Features, UI, animations
- **Testing** (15%): Unit tests, widget tests, integration tests
- **Release Management** (10%): App Store submissions, versioning
- **Bug Fixes** (5%): Respond to crashes, user reports

**Success Metrics**:

- App store rating: 4.5+ stars
- Crash-free rate: 99.5%+
- App size: <50MB
- Cold start time: <3 seconds
- Feature parity: 100% with web version

**Skills Required**:

- Flutter & Dart
- iOS & Android development
- RESTful APIs
- Push notifications (Firebase)
- App Store deployment

**Compensation** (Year 1):

- Salary: $100K-130K
- Equity: 0.1-0.5%
- Bonus: 10%

---

### ML Engineer

**Hired**: Month 1-3 (first hire)  
**Reports To**: VP Data & AI  
**Direct Reports**: None

**Responsibilities**:

- Train and deploy ML models (LSTM price prediction, FinBERT sentiment)
- Build data pipelines (ETL, feature engineering)
- Optimize model inference (latency <5 seconds)
- Evaluate model performance (accuracy, precision, recall)
- Integrate AI models with backend services
- Self-host models to reduce OpenAI costs

**Key Duties**:

- **Model Development** (50%): Train, tune, evaluate models
- **MLOps** (25%): Deploy models, monitor performance, A/B testing
- **Data Engineering** (20%): ETL pipelines, feature stores
- **Research** (5%): Read papers, experiment with new techniques

**Success Metrics**:

- Model accuracy: 87%+ on A-grade signals
- Inference latency: <5 seconds
- Cost per prediction: <$0.05
- Model uptime: 99.9%
- Experiment velocity: 10+ experiments per month

**Skills Required**:

- Machine learning (PyTorch, TensorFlow, scikit-learn)
- NLP (transformers, BERT, sentiment analysis)
- Time-series forecasting (LSTM, Prophet)
- MLOps (Docker, Kubernetes, model serving)
- Python (pandas, numpy, scipy)

**Compensation** (Year 1):

- Salary: $130K-160K
- Equity: 0.25-1%
- Bonus: 15%

---

### DevOps / Infrastructure Engineer

**Hired**: Month 6-9  
**Reports To**: CTO or VP Engineering  
**Direct Reports**: None

**Responsibilities**:

- Manage AWS infrastructure (EC2, RDS, S3, CloudFront)
- Set up CI/CD pipelines (GitHub Actions, ArgoCD)
- Implement infrastructure as code (Terraform)
- Monitor system health (Datadog, CloudWatch, PagerDuty)
- Optimize cloud costs (reserved instances, spot instances)
- Ensure security (VPCs, security groups, secrets management)

**Key Duties**:

- **Infrastructure Management** (40%): Provision servers, databases, networking
- **CI/CD** (25%): Build pipelines, deployment automation
- **Monitoring** (20%): Set up alerts, dashboards, on-call
- **Cost Optimization** (10%): Analyze spend, right-size instances
- **Security** (5%): Patches, compliance, penetration testing

**Success Metrics**:

- Deployment frequency: 10+ per week
- Deployment success rate: 99%+
- Mean time to recovery (MTTR): <30 minutes
- Cloud cost per user: <$2/month
- Security incidents: Zero

**Skills Required**:

- AWS (EC2, RDS, S3, Lambda, CloudFront)
- Infrastructure as code (Terraform, CloudFormation)
- CI/CD (GitHub Actions, Jenkins, ArgoCD)
- Kubernetes & Docker
- Monitoring (Datadog, Prometheus, Grafana)

**Compensation** (Year 1):

- Salary: $110K-140K
- Equity: 0.1-0.5%
- Bonus: 10%

---

## Product & Design Department

### Product Manager

**Hired**: Month 3-6 (first hire), then scale to 4 by Month 18  
**Reports To**: CPO  
**Direct Reports**: None (works cross-functionally)

**Responsibilities**:

- Own specific product areas (e.g., Briefing Experience, Portfolio Alerts, Community)
- Write product requirement documents (PRDs)
- Define user stories and acceptance criteria
- Prioritize backlog with engineering
- Conduct user research (interviews, surveys)
- Analyze product metrics and iterate
- Collaborate with designers on UI/UX

**Key Duties**:

- **Product Planning** (35%): PRDs, user stories, roadmap
- **User Research** (25%): Interviews, surveys, usability tests
- **Analytics** (20%): SQL queries, dashboards, A/B tests
- **Cross-Functional Collaboration** (15%): Work with eng, design, marketing
- **Launches** (5%): Go-to-market planning, feature announcements

**Success Metrics**:

- Feature adoption: 60%+ within 30 days
- User satisfaction: 4+ stars for owned features
- Velocity: Ship features on time (90%+)
- Data-driven decisions: Every feature has success metrics

**Skills Required**:

- Product management (PRDs, user stories, prioritization)
- Data analysis (SQL, Mixpanel, A/B testing)
- User research (interviews, surveys)
- Wireframing (Figma, Sketch)
- Communication (stakeholder management)

**Compensation** (Year 1):

- Salary: $100K-130K
- Equity: 0.1-0.5%
- Bonus: 10%

---

### Product Designer (UI/UX)

**Hired**: Month 1-3 (first hire)  
**Reports To**: Head of Design or CPO  
**Direct Reports**: None

**Responsibilities**:

- Design user interfaces for mobile app, email, web
- Create wireframes, mockups, prototypes
- Build and maintain design system (components, colors, typography)
- Conduct usability testing
- Collaborate with engineers on implementation
- Ensure brand consistency across all touchpoints

**Key Duties**:

- **UI Design** (50%): Mockups, prototypes, design system
- **UX Research** (20%): Usability tests, user flows
- **Collaboration** (20%): Work with PMs and engineers
- **Iteration** (10%): Respond to feedback, A/B test designs

**Success Metrics**:

- Design delivery: On time (95%+)
- User satisfaction: 4.5+ app store rating
- Design system adoption: 100% of components used
- Usability test success rate: 80%+ task completion

**Skills Required**:

- UI/UX design (Figma, Sketch, Adobe XD)
- Prototyping (Figma, InVision, Principle)
- Design systems (components, tokens)
- User research (usability testing, user flows)
- HTML/CSS (basic understanding for handoff)

**Compensation** (Year 1):

- Salary: $90K-120K
- Equity: 0.1-0.5%
- Bonus: 10%

---

## Data & AI Department

### Data Scientist

**Hired**: Month 6-12 (2 hires initially)  
**Reports To**: VP Data & AI  
**Direct Reports**: None

**Responsibilities**:

- Analyze user behavior and market patterns
- Build predictive models (price movements, user churn)
- Conduct experiments and A/B tests
- Create dashboards and reports for stakeholders
- Collaborate with ML engineers on model development
- Research alternative data sources

**Key Duties**:

- **Analysis** (40%): Exploratory data analysis, pattern discovery
- **Modeling** (30%): Build models, feature engineering
- **Experimentation** (20%): A/B tests, statistical analysis
- **Reporting** (10%): Dashboards, presentations, insights

**Success Metrics**:

- Insights delivered: 5+ actionable insights per month
- Model accuracy: 85%+ on predictions
- Experiment velocity: 10+ experiments per quarter
- Stakeholder satisfaction: 4+ stars

**Skills Required**:

- Statistics & machine learning
- Python (pandas, scikit-learn, statsmodels)
- SQL (complex queries, window functions)
- Data visualization (Tableau, Looker, Matplotlib)
- Experimentation (A/B testing, hypothesis testing)

**Compensation** (Year 1):

- Salary: $110K-140K
- Equity: 0.1-0.5%
- Bonus: 10%

---

### Data Engineer

**Hired**: Month 9-12  
**Reports To**: VP Data & AI  
**Direct Reports**: None

**Responsibilities**:

- Build ETL pipelines (extract, transform, load)
- Manage data warehouse (Snowflake or BigQuery)
- Integrate alternative data sources (Planet Labs, SafeGraph)
- Ensure data quality and consistency
- Optimize data storage and query performance
- Build real-time data streaming (Kafka, Kinesis)

**Key Duties**:

- **Pipeline Development** (50%): ETL jobs, data integration
- **Data Quality** (20%): Validation, monitoring, alerts
- **Performance Optimization** (15%): Query tuning, indexing
- **Infrastructure** (10%): Data warehouse, storage
- **Documentation** (5%): Data dictionaries, schemas

**Success Metrics**:

- Data freshness: <24 hours for all sources
- Pipeline reliability: 99.9% uptime
- Data quality: <0.1% error rate
- Query performance: <5 seconds for dashboards

**Skills Required**:

- ETL tools (Airflow, Fivetran, dbt)
- Databases (PostgreSQL, MongoDB, Snowflake)
- Python (pandas, PySpark)
- Data modeling (star schema, data lakes)
- Cloud data services (AWS Glue, S3, Redshift)

**Compensation** (Year 1):

- Salary: $110K-140K
- Equity: 0.1-0.5%
- Bonus: 10%

---

## Marketing & Growth Department

### Growth Marketing Manager

**Hired**: Month 3-6  
**Reports To**: CMO (or CEO initially)  
**Direct Reports**: Performance Marketers (2-3 by Month 12)

**Responsibilities**:

- Drive user acquisition across all channels
- Manage paid advertising (Facebook, Google, TikTok)
- Optimize conversion funnels (signup, activation, paid conversion)
- Build referral and viral growth loops
- Manage marketing budget and track ROI
- Analyze CAC, LTV, and marketing metrics

**Key Duties**:

- **Paid Acquisition** (40%): Facebook/Google ads, campaign optimization
- **Conversion Optimization** (25%): Landing pages, signup flow, A/B tests
- **Analytics** (20%): CAC, LTV, attribution, funnel analysis
- **Referral Programs** (10%): Design loops, incentive structures
- **Reporting** (5%): Weekly metrics, forecasts

**Success Metrics**:

- User acquisition: 10K → 50K → 150K (on roadmap)
- CAC: <$25 blended
- Paid conversion rate: 40% → 70%
- LTV/CAC: >10x
- Referral rate: 20%+ of users refer a friend

**Skills Required**:

- Performance marketing (Facebook Ads, Google Ads)
- Analytics (Google Analytics, Mixpanel, attribution)
- Conversion optimization (landing pages, A/B testing)
- Growth hacking (viral loops, referral programs)
- SQL & Excel (data analysis)

**Compensation** (Year 1):

- Salary: $90K-120K
- Equity: 0.1-0.5%
- Bonus: 20% (tied to CAC, user growth)

---

### Content Marketing Manager

**Hired**: Month 6-12  
**Reports To**: CMO  
**Direct Reports**: Content Writers (2)

**Responsibilities**:

- Create blog posts, videos, infographics, guides
- Build SEO strategy (keyword research, backlinks)
- Manage social media (Twitter, LinkedIn, YouTube)
- Produce educational content (how to invest, market analysis)
- Partner with influencers and podcasts
- Build email newsletter (growth, engagement)

**Key Duties**:

- **Content Creation** (50%): Blog posts, videos, social media
- **SEO** (20%): Keyword research, optimization, backlinks
- **Social Media** (15%): Posting, engagement, community management
- **Partnerships** (10%): Influencers, podcasts, guest posts
- **Analytics** (5%): Traffic, engagement, conversions

**Success Metrics**:

- Organic traffic: 50K visits/month by Year 2
- SEO ranking: Top 10 for 50+ keywords
- Social followers: 50K+ combined (Twitter, LinkedIn, YouTube)
- Content conversion: 5%+ of readers sign up
- Email subscribers: 100K+ by Year 2

**Skills Required**:

- Content writing (blog posts, scripts, social)
- SEO (keyword research, on-page, backlinks)
- Social media marketing
- Video editing (basic)
- Analytics (Google Analytics, SEMrush)

**Compensation** (Year 1):

- Salary: $80K-110K
- Equity: 0.05-0.3%
- Bonus: 10%

---

## Sales & Partnerships Department

### Enterprise Sales Rep

**Hired**: Month 12-18 (3-5 reps by Year 2)  
**Reports To**: VP Sales  
**Direct Reports**: None

**Responsibilities**:

- Sell Brief Enterprise tier to financial advisors and institutions
- Conduct demos and product presentations
- Negotiate contracts and close deals
- Build sales pipeline (cold outreach, warm intros)
- Collaborate with product on enterprise features
- Provide customer feedback to product team

**Key Duties**:

- **Prospecting** (30%): Cold emails, LinkedIn outreach, conferences
- **Demos** (30%): Product presentations, Q&A, objection handling
- **Closing** (25%): Negotiations, contracts, onboarding
- **Account Management** (10%): Upsells, renewals, feedback
- **Reporting** (5%): CRM updates, pipeline forecasts

**Success Metrics**:

- Deals closed: $500K ARR by Year 2 (per rep)
- Win rate: 20%+ (demos to closed deals)
- Pipeline: 3x quota in pipeline at all times
- Average deal size: $5K-25K ACV

**Skills Required**:

- B2B SaaS sales
- Financial services domain knowledge
- CRM (Salesforce, HubSpot)
- Demo presentation skills
- Negotiation & closing

**Compensation** (Year 2):

- Salary: $80K-100K base
- Commission: $40K-80K (OTE $120-180K)
- Equity: 0.05-0.2%

---

### Broker Partnerships Manager

**Hired**: Month 6-12  
**Reports To**: VP Sales  
**Direct Reports**: None

**Responsibilities**:

- Negotiate partnerships with 30+ brokers (Hatch, Stake, Robinhood, etc.)
- Integrate broker APIs (OAuth, account linking)
- Track affiliate revenue (CPA, revenue share)
- Optimize conversion rates (recommendations, KYC assistance)
- Build co-marketing campaigns with brokers
- Manage contracts and renewals

**Key Duties**:

- **Partnership Negotiations** (40%): Outreach, contracts, pricing
- **Integration** (25%): API integration, testing, QA
- **Revenue Tracking** (20%): Attribution, payouts, reporting
- **Optimization** (10%): A/B test recommendations, improve conversion
- **Relationship Management** (5%): Quarterly business reviews

**Success Metrics**:

- Broker partnerships: 30+ live integrations
- Affiliate revenue: $300K (Year 1) → $13.65M (Year 3)
- Conversion rate: 60% → 75% (users sign up with recommended broker)
- Average CPA: $50 → $75 (negotiate better rates)

**Skills Required**:

- Partnership negotiation
- API integration (OAuth, webhooks)
- Financial services domain knowledge
- Data analysis (attribution, conversion funnels)
- Relationship management

**Compensation** (Year 1):

- Salary: $90K-120K
- Equity: 0.1-0.5%
- Bonus: 15% + commission on affiliate revenue

---

## Customer Success Department

### Customer Support Lead

**Hired**: Month 6-9  
**Reports To**: VP Customer Success (or CEO initially)  
**Direct Reports**: Customer Support Reps (3-8 by Year 2)

**Responsibilities**:

- Build customer support function (email, chat, phone)
- Set up help desk system (Zendesk, Intercom)
- Respond to user questions and issues (<2 hour response time)
- Create help center articles and FAQs
- Track customer satisfaction (CSAT, NPS)
- Escalate bugs and feature requests to product/engineering
- Train support team

**Key Duties**:

- **Support Operations** (40%): Respond to tickets, manage queue
- **Team Leadership** (25%): Hire, train, 1-on-1s, performance reviews
- **Process Improvement** (20%): SOPs, macros, workflows
- **Reporting** (10%): CSAT, response time, ticket volume
- **Collaboration** (5%): Work with product on issues, feedback

**Success Metrics**:

- Response time: <2 hours (avg), <15 min (urgent)
- Resolution time: <24 hours (90% of tickets)
- CSAT: 4.5+ stars
- First contact resolution: 80%+
- Ticket volume per user: <0.1/month (low = good product)

**Skills Required**:

- Customer support experience
- Help desk tools (Zendesk, Intercom, Freshdesk)
- Communication (empathy, clarity, patience)
- Team leadership (hiring, training)
- Process optimization

**Compensation** (Year 1):

- Salary: $70K-90K
- Equity: 0.05-0.3%
- Bonus: 10%

---

### Customer Onboarding Specialist

**Hired**: Month 12-18  
**Reports To**: Customer Support Lead  
**Direct Reports**: None

**Responsibilities**:

- Guide new users through first briefing experience
- Conduct onboarding calls for Premium/Pro users
- Create onboarding email sequences
- Track activation metrics (time to value)
- Provide personalized tips and recommendations
- Gather feedback during onboarding

**Key Duties**:

- **Onboarding Calls** (40%): 1-on-1 sessions with Premium users
- **Email Sequences** (25%): Write onboarding drip campaigns
- **Analytics** (20%): Track activation, engagement, churn
- **Feedback Collection** (10%): Surveys, interviews
- **Documentation** (5%): Help articles, videos

**Success Metrics**:

- Activation rate: 80%+ (users complete onboarding)
- Time to value: <5 minutes (signup to first briefing)
- Onboarded user retention: 85%+ (30-day)
- CSAT for onboarding: 4.5+ stars

**Skills Required**:

- Customer success / onboarding experience
- Communication (clear, helpful)
- Data analysis (activation funnels)
- Educational content creation
- CRM tools (Intercom, HubSpot)

**Compensation** (Year 2):

- Salary: $60K-80K
- Equity: 0.05-0.2%
- Bonus: 10%

---

## Operations & Finance Department

### Finance Manager

**Hired**: Month 9-12  
**Reports To**: CFO (or CEO initially)  
**Direct Reports**: Accounting (outsourced initially)

**Responsibilities**:

- Manage day-to-day financial operations
- Process payroll, AP/AR, expenses
- Prepare monthly financial reports
- Manage banking relationships
- Assist with fundraising (financial models, data room)
- Ensure compliance with tax regulations

**Key Duties**:

- **Financial Reporting** (30%): Monthly P&L, cash flow, balance sheet
- **Operations** (30%): Payroll, AP/AR, reconciliation
- **Budgeting** (20%): Track actuals vs budget, forecasts
- **Compliance** (15%): Tax filings, audit support
- **Fundraising Support** (5%): Financial models, due diligence

**Success Metrics**:

- Reports delivered on time: 100%
- Payroll accuracy: 100%
- Budget variance: <5%
- Tax filings: On time, zero penalties

**Skills Required**:

- Accounting (GAAP, financial statements)
- Financial modeling (Excel, scenario analysis)
- Payroll systems (Gusto, ADP)
- Accounting software (QuickBooks, Xero, NetSuite)
- Compliance (tax, audit)

**Compensation** (Year 1):

- Salary: $80K-110K
- Equity: 0.05-0.3%
- Bonus: 10%

---

### Operations Manager

**Hired**: Month 12-18  
**Reports To**: CEO or COO  
**Direct Reports**: Office Manager, IT Support

**Responsibilities**:

- Manage daily operations (office, IT, vendors)
- Negotiate vendor contracts (software, tools, services)
- Implement operational processes and tools
- Coordinate company events (all-hands, offsites)
- Manage benefits and HR administration
- Support hiring and onboarding

**Key Duties**:

- **Vendor Management** (30%): Negotiate, manage, optimize costs
- **Processes** (25%): SOPs, workflows, automation
- **HR Administration** (20%): Benefits, onboarding, policies
- **Office Management** (15%): Space, equipment, logistics
- **Events** (10%): All-hands, team offsites, recruiting events

**Success Metrics**:

- Vendor cost savings: 10% reduction annually
- Process documentation: 100% of critical processes documented
- Employee satisfaction: 4+ stars on benefits, onboarding
- Event execution: On time, on budget

**Skills Required**:

- Operations management
- Vendor negotiation
- Project management
- HR administration
- Process optimization

**Compensation** (Year 2):

- Salary: $80K-110K
- Equity: 0.05-0.3%
- Bonus: 10%

---

## Legal & Compliance Department

### Compliance Manager

**Hired**: Month 12-18  
**Reports To**: General Counsel  
**Direct Reports**: None

**Responsibilities**:

- Ensure all content is compliant ("observations not advice")
- Review marketing materials, emails, social posts
- Manage SOC 2 Type II certification process
- Monitor regulatory changes (SEC, FMA, ASIC, FCA)
- Train team on compliance requirements
- Handle user complaints and disputes

**Key Duties**:

- **Content Review** (40%): Review all user-facing content
- **SOC 2** (25%): Implement controls, prepare for audit
- **Regulatory Monitoring** (20%): Track law changes, assess impact
- **Training** (10%): Educate team on compliance
- **Dispute Resolution** (5%): Handle complaints

**Success Metrics**:

- Zero regulatory violations
- SOC 2 certification: Achieved on schedule
- Content review turnaround: <2 business days
- Compliance training: 100% of employees trained

**Skills Required**:

- Financial services compliance
- Securities law (RIA, broker-dealer regulations)
- Data protection (GDPR, CCPA)
- SOC 2 / ISO 27001
- Risk management

**Compensation** (Year 2):

- Salary: $100K-130K
- Equity: 0.05-0.3%
- Bonus: 10%

---

## Hiring Timeline

### Year 1 (Months 0-12): 20 People

| Role                         | Count  | Month Hired |
| ---------------------------- | ------ | ----------- |
| Founders (CEO, CTO, CPO)     | 3      | Month 0     |
| Senior Backend Engineer      | 3      | Months 1-3  |
| ML Engineer                  | 1      | Month 1     |
| Product Designer             | 1      | Month 2     |
| Mobile Engineer (Flutter)    | 2      | Months 3-6  |
| Product Manager              | 1      | Month 4     |
| VP Data & AI                 | 1      | Month 3     |
| Growth Marketing Manager     | 1      | Month 6     |
| DevOps Engineer              | 1      | Month 6     |
| Customer Support Lead        | 1      | Month 6     |
| Broker Partnerships Manager  | 1      | Month 9     |
| Data Scientist               | 2      | Months 9-12 |
| Backend Engineer (Mid-level) | 2      | Months 9-12 |
| **Total**                    | **20** |             |

### Year 2 (Months 13-24): 40 People (+20)

| Role                        | Count                           | Month Hired  |
| --------------------------- | ------------------------------- | ------------ |
| VP Engineering (Backend)    | 1                               | Month 12     |
| CMO                         | 1                               | Month 15     |
| CFO                         | 1                               | Month 18     |
| General Counsel (part-time) | 1                               | Month 12     |
| Backend Engineers           | 5                               | Months 13-18 |
| Mobile Engineers            | 2                               | Months 13-18 |
| Data Scientists             | 2                               | Months 13-18 |
| ML Engineers                | 2                               | Months 13-18 |
| Product Managers            | 2                               | Months 13-18 |
| Designers                   | 2                               | Months 13-18 |
| Enterprise Sales Reps       | 3                               | Months 15-20 |
| Performance Marketers       | 2                               | Months 13-18 |
| Content Writers             | 2                               | Months 13-18 |
| Customer Support Reps       | 5                               | Months 13-20 |
| Finance Manager             | 1                               | Month 12     |
| Operations Manager          | 1                               | Month 15     |
| **Total New Hires**         | **33**                          |              |
| **Cumulative**              | **53** (attrition) → **40 net** |

### Year 3 (Months 25-36): 100 People (+60)

**Scaling across all departments**: Engineering (50), Product (10), Data/AI (15), Marketing (12), Sales (8), Customer Success (15), Operations (5), Legal (3)

---

## Compensation Structure

### Salary Bands (Auckland/NZ Base, USD Equivalent)

| Level              | Salary Range | Equity Range |
| ------------------ | ------------ | ------------ |
| **C-Suite**        | $150K-220K   | 0.5-10%      |
| **VP / Head of**   | $140K-180K   | 0.5-3%       |
| **Senior Manager** | $110K-150K   | 0.25-1.5%    |
| **Manager**        | $90K-130K    | 0.1-1%       |
| **Senior IC**      | $110K-160K   | 0.1-0.5%     |
| **Mid-Level IC**   | $80K-120K    | 0.05-0.3%    |
| **Junior IC**      | $60K-90K     | 0.01-0.1%    |

**Notes**:

- Salaries 10-20% higher for US-based roles (SF, NYC)
- Equity vests over 4 years (1-year cliff, monthly after)
- Bonuses: 10-30% of salary (based on role, performance)

### Equity Pool

- **Founders**: 60-70% (20-30% each)
- **Employee Pool**: 15-20% (refreshed after each round)
- **Investors**: 15-25% (after 3 funding rounds)

---

## Company Culture & Values

### Core Values

1. **Transparency** 🔍

   - Open metrics (share MRR, churn, CAC with team)
   - Honest communication (good news and bad)
   - Open salary bands (everyone knows ranges)

2. **User Obsession** 💙

   - Users first, always
   - Talk to 10+ users per week (everyone)
   - Build what users need, not what we think is cool

3. **Excellence** 🏆

   - High bar for quality (code, design, content)
   - Ship fast, but ship right
   - 87% accuracy = institutional grade

4. **Ownership** 🚀

   - Own outcomes, not tasks
   - No "that's not my job" mentality
   - Fix what's broken, don't wait

5. **Continuous Learning** 📚
   - Finance, AI, markets change daily
   - $1K/year learning budget per employee
   - Weekly knowledge sharing (Friday demos)

### Work Culture

- **Remote-first**: Hire globally, office optional
- **Async communication**: Default to written (Notion, Slack)
- **Focus time**: No meetings Tuesday/Thursday afternoons
- **All-hands**: Weekly (Mondays, 30 min)
- **Offsites**: Quarterly team retreats
- **Unlimited PTO**: Trust-based (minimum 15 days/year)
- **Equipment**: $2K laptop + $500 home office budget

---

**This organizational structure will scale Brief from 3 founders to 180 employees over 5 years, achieving $158M revenue and $60M profit by Year 5.** 🚀
