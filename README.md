# ShopIt

ShopIt is a cloud-based shopping application built around Python, AI, and cloud infrastructure.

The project focuses on building a complete product while integrating backend development, databases, cloud deployment, payments, and AI-powered shopping functionality.

## Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic Settings

### Database

- PostgreSQL
- Redis

### Infrastructure

- Docker
- Cloud deployment

### Integrations

- Razorpay
- AI API

## Repository Structure

```text
shopit/
├── backend/
├── frontend/
├── docs/
├── .env.example
├── .gitignore
├── README.md
└── docker-compose.yml
```

## Backend Structure

```text
backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── tests/
├── requirements.txt
└── .venv/
```

`.venv/` is local development infrastructure and is not committed to the repository.

## Configuration

ShopIt uses environment variables for configuration and secrets.

The repository contains:

```text
.env.example
```

Developers should create their local:

```text
.env
```

from the example file.

Secrets and environment-specific configuration must never be committed to Git.

## Project Status

- Under active development

The project is being developed incrementally, with each phase producing a working part of the final product.