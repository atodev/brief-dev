# Project Structure - Brief Application

## Repository Organization

```
Fin-Advisor/
├── README.md
├── LICENSE
├── .gitignore
├── docker-compose.yml
├── docs/
│   ├── ARCHITECTURE.md
│   ├── TECH_STACK.md
│   ├── ROADMAP.md
│   ├── DATA_SOURCES.md
│   ├── API_DOCUMENTATION.md
│   └── DEPLOYMENT.md
│
├── frontend/
│   ├── web/                      # React web application
│   │   ├── public/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   ├── pages/
│   │   │   ├── services/
│   │   │   ├── hooks/
│   │   │   ├── store/
│   │   │   ├── utils/
│   │   │   ├── types/
│   │   │   ├── App.tsx
│   │   │   └── main.tsx
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── vite.config.ts
│   │
│   └── mobile/                   # Flutter mobile app
│       ├── android/
│       ├── ios/
│       ├── lib/
│       │   ├── main.dart
│       │   ├── app.dart
│       │   ├── core/
│       │   │   ├── config/
│       │   │   ├── constants/
│       │   │   ├── theme/
│       │   │   └── utils/
│       │   ├── data/
│       │   │   ├── models/
│       │   │   ├── repositories/
│       │   │   └── data_sources/
│       │   ├── domain/
│       │   │   ├── entities/
│       │   │   ├── repositories/
│       │   │   └── use_cases/
│       │   ├── presentation/
│       │   │   ├── pages/
│       │   │   ├── widgets/
│       │   │   └── providers/
│       │   └── services/
│       ├── pubspec.yaml
│       └── analysis_options.yaml
│
├── backend/
│   ├── services/
│   │   ├── user-service/        # Node.js/NestJS
│   │   │   ├── src/
│   │   │   │   ├── modules/
│   │   │   │   ├── common/
│   │   │   │   ├── config/
│   │   │   │   └── main.ts
│   │   │   ├── test/
│   │   │   ├── package.json
│   │   │   ├── tsconfig.json
│   │   │   └── Dockerfile
│   │   │
│   │   ├── portfolio-service/   # Node.js/NestJS
│   │   │   ├── src/
│   │   │   ├── test/
│   │   │   ├── package.json
│   │   │   └── Dockerfile
│   │   │
│   │   ├── trade-service/       # Node.js/NestJS
│   │   │   ├── src/
│   │   │   ├── test/
│   │   │   ├── package.json
│   │   │   └── Dockerfile
│   │   │
│   │   ├── market-data-service/ # Python/FastAPI
│   │   │   ├── app/
│   │   │   │   ├── api/
│   │   │   │   ├── core/
│   │   │   │   ├── models/
│   │   │   │   ├── services/
│   │   │   │   └── main.py
│   │   │   ├── tests/
│   │   │   ├── requirements.txt
│   │   │   └── Dockerfile
│   │   │
│   │   ├── ai-analysis-service/ # Python/FastAPI
│   │   │   ├── app/
│   │   │   │   ├── ml_models/
│   │   │   │   ├── api/
│   │   │   │   ├── services/
│   │   │   │   └── main.py
│   │   │   ├── notebooks/       # Jupyter notebooks for research
│   │   │   ├── models/          # Saved ML models
│   │   │   ├── tests/
│   │   │   ├── requirements.txt
│   │   │   └── Dockerfile
│   │   │
│   │   ├── news-service/        # Python/FastAPI
│   │   │   ├── app/
│   │   │   ├── tests/
│   │   │   ├── requirements.txt
│   │   │   └── Dockerfile
│   │   │
│   │   ├── alert-service/       # Node.js/NestJS
│   │   │   ├── src/
│   │   │   ├── test/
│   │   │   ├── package.json
│   │   │   └── Dockerfile
│   │   │
│   │   └── compliance-service/  # Node.js/NestJS
│   │       ├── src/
│   │       ├── test/
│   │       ├── package.json
│   │       └── Dockerfile
│   │
│   ├── shared/
│   │   ├── proto/               # gRPC proto files
│   │   ├── types/               # Shared TypeScript types
│   │   └── utils/               # Shared utilities
│   │
│   └── api-gateway/             # Kong or custom gateway
│       ├── config/
│       └── plugins/
│
├── ml/
│   ├── training/                # Training scripts
│   │   ├── price_prediction/
│   │   ├── sentiment_analysis/
│   │   ├── portfolio_optimization/
│   │   └── anomaly_detection/
│   ├── notebooks/               # Research notebooks
│   ├── data/                    # Training data
│   ├── models/                  # Saved models
│   ├── mlflow/                  # MLflow tracking
│   └── requirements.txt
│
├── data/
│   ├── ingestion/               # Data ingestion scripts
│   │   ├── crypto/
│   │   ├── forex/
│   │   ├── stocks/
│   │   ├── commodities/
│   │   └── news/
│   ├── processing/              # ETL pipelines
│   └── schemas/                 # Database schemas
│
├── infrastructure/
│   ├── terraform/               # Infrastructure as Code
│   │   ├── modules/
│   │   ├── environments/
│   │   │   ├── dev/
│   │   │   ├── staging/
│   │   │   └── production/
│   │   └── main.tf
│   │
│   ├── kubernetes/              # K8s manifests
│   │   ├── base/
│   │   ├── overlays/
│   │   │   ├── dev/
│   │   │   ├── staging/
│   │   │   └── production/
│   │   └── helm/
│   │
│   ├── ansible/                 # Configuration management
│   │   ├── playbooks/
│   │   └── roles/
│   │
│   └── scripts/                 # Deployment scripts
│       ├── deploy.sh
│       ├── rollback.sh
│       └── backup.sh
│
├── monitoring/
│   ├── prometheus/              # Prometheus config
│   ├── grafana/                 # Grafana dashboards
│   └── alerting/                # Alert rules
│
├── tests/
│   ├── e2e/                     # End-to-end tests
│   ├── integration/             # Integration tests
│   ├── load/                    # Load tests (k6)
│   └── security/                # Security tests
│
├── scripts/
│   ├── setup/                   # Setup scripts
│   ├── migration/               # Database migrations
│   ├── seed/                    # Seed data
│   └── utils/                   # Utility scripts
│
└── .github/
    ├── workflows/               # GitHub Actions CI/CD
    │   ├── backend-ci.yml
    │   ├── frontend-ci.yml
    │   ├── mobile-ci.yml
    │   ├── deploy-staging.yml
    │   └── deploy-production.yml
    └── ISSUE_TEMPLATE/
```

## Key Directories Explained

### `/frontend`

Contains all client-side applications. Separated into web (React) and mobile (Flutter) for clear organization.

### `/backend/services`

Microservices architecture with each service in its own directory. Services are independent and can be deployed separately.

### `/ml`

Machine learning code separated from backend services. Includes training scripts, notebooks for research, and model artifacts.

### `/data`

Data pipeline code including ingestion, processing, and schemas. Keeps data engineering separate from application code.

### `/infrastructure`

All infrastructure-as-code and deployment configurations. Supports multiple environments (dev, staging, production).

### `/monitoring`

Observability configuration for metrics, logging, and alerting.

### `/tests`

Cross-service tests including E2E, integration, and load testing.

## Development Workflow

### 1. Local Development

```bash
# Start databases and dependencies
docker-compose up -d

# Start backend services (in separate terminals)
cd backend/services/user-service && npm run dev
cd backend/services/market-data-service && python app/main.py

# Start frontend
cd frontend/web && npm run dev
cd frontend/mobile && flutter run
```

### 2. Testing

```bash
# Unit tests
npm test                        # Node.js services
pytest                          # Python services
flutter test                    # Flutter app

# Integration tests
npm run test:integration

# E2E tests
cd tests/e2e && npm test
```

### 3. Building

```bash
# Build Docker images
docker build -t brief/user-service backend/services/user-service

# Build Flutter app
cd frontend/mobile
flutter build apk             # Android
flutter build ios             # iOS
```

### 4. Deployment

```bash
# Deploy to staging
./infrastructure/scripts/deploy.sh staging

# Deploy to production
./infrastructure/scripts/deploy.sh production
```

## Configuration Management

### Environment Variables

Each service has its own `.env` file:

- `.env.development`
- `.env.staging`
- `.env.production`

### Secrets Management

- Development: `.env` files (gitignored)
- Production: AWS Secrets Manager or HashiCorp Vault

## Naming Conventions

### Code

- **Services**: kebab-case (user-service, market-data-service)
- **Files**: camelCase.ts (TypeScript), snake_case.py (Python)
- **Classes**: PascalCase
- **Functions**: camelCase (JS/TS), snake_case (Python)
- **Constants**: UPPER_SNAKE_CASE

### Database

- **Tables**: snake_case (users, portfolio_positions)
- **Columns**: snake_case (user_id, created_at)

### API

- **Endpoints**: kebab-case (/api/v1/market-data, /api/v1/user-portfolio)
- **Query params**: camelCase or snake_case (consistently)

## Next Steps

1. Initialize Git repository
2. Set up CI/CD pipelines
3. Create development environment
4. Start with user-service implementation
5. Build out data ingestion layer
6. Develop ML models
7. Create mobile app prototype

Would you like me to create any specific part of this structure or help you get started with implementation?
