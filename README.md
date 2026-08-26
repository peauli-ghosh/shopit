# ShopIt

ShopIt is an AI-powered shopping platform designed to help users discover, understand, compare, and purchase products through a single web application.

The goal is to build a complete, production-oriented shopping product where users can browse products, search for what they need, receive AI-assisted recommendations and insights, manage their shopping activity, and complete purchases securely.

The application is built with Python as the primary backend technology, with AI integrated into the shopping experience and cloud infrastructure used for deployment, data, and file storage.

## Core Product Goals

ShopIt focuses on:

- Product discovery and search
- AI-assisted shopping and recommendations
- Product comparison and analysis
- User accounts and personalized shopping activity
- Secure online payments
- Cloud-based application and data infrastructure
- A scalable Python backend

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