# MediDeploy — Multi-Environment CI/CD Pipeline

A production-grade CI/CD pipeline built on GitHub Actions, demonstrating
automated testing, environment promotion, and deployment gates.

---

## The Problem This Solves

In any serious engineering team, code never goes directly from a developer's
laptop to production. It travels through a controlled pipeline — tested,
reviewed, and approved at every stage. This project implements that pipeline
from scratch.

---

## Pipeline Architecture
Every stage is a gate. Nothing moves forward without passing the previous one.

---

## The Medical Analogy

This pipeline mirrors a hospital's drug approval process:

| Pipeline Stage | Hospital Equivalent |
|---|---|
| `develop` branch | Research lab — fast iteration, safe to experiment |
| CI gate | Ethics board — automated checks before anything moves |
| `staging` branch | Clinical trial — controlled environment mirroring production |
| Production approval gate | Consultant sign-off — human in the loop for high-risk changes |
| `main` branch | Patient — only receives thoroughly validated treatment |

---

## Project Structure

medideploy/
├── app/
│   ├── main.py          # Flask API with /health and /vitals endpoints
│   └── config.py        # Per-environment configuration
├── tests/
│   └── test_vitals.py   # Unit tests for all endpoints
├── environments/
│   ├── dev.env          # Dev environment variables
│   ├── staging.env      # Staging environment variables
│   └── prod.env         # Production environment variables
├── .github/workflows/
│   ├── ci.yml           # Runs on every PR — lint, test, health check
│   ├── deploy-dev.yml   # Triggers on merge to develop
│   ├── deploy-staging.yml # Triggers on merge to staging
│   └── deploy-prod.yml  # Triggers on merge to main + manual approval
└── Makefile             # Developer shortcuts

---

## Workflows

### CI Pipeline (`ci.yml`)
Triggers on every pull request targeting `develop`, `staging`, or `main`.

Runs:
- `flake8` linting
- Full `pytest` test suite
- Health endpoint smoke test

A failing check blocks the merge. No exceptions.

### Deploy to Dev (`deploy-dev.yml`)
Triggers automatically on every push to `develop`. Loads `dev.env`,
confirms environment, logs commit SHA and actor for full auditability.

### Deploy to Staging (`deploy-staging.yml`)
Triggers automatically on merge to `staging`. Mirrors production
configuration. Runs full test suite before deployment.

### Deploy to Production (`deploy-prod.yml`)
Triggers on merge to `main`. Requires manual approval via GitHub
Environments before executing. This is the production gate.

---

## API Endpoints

| Endpoint | Method | Response |
|---|---|---|
| `/health` | GET | `{"status": "ok"}` |
| `/vitals` | GET | Heart rate, blood pressure, temperature, environment name |

The `/vitals` endpoint returns the current `environment` in its response —
making it easy to confirm the correct version is running in each environment.

---

## Quick Start

```bash
# Clone and set up
git clone https://github.com/YOUR_USERNAME/medideploy.git
cd medideploy
python3 -m venv venv
source venv/bin/activate
make install

# Run locally
make run

# Run tests
make test

# Lint
make lint
```

---

## Branch Strategy

| Branch | Purpose | Deploys to |
|---|---|---|
| `develop` | Active development | Dev environment |
| `staging` | Pre-production validation | Staging environment |
| `main` | Production-ready code | Production (with approval) |

All branches are protected. Direct pushes are blocked. Everything
goes through a pull request.

---

## Tech Stack

- **Python 3.11** + **Flask** — application
- **pytest** — testing
- **flake8** — linting
- **GitHub Actions** — CI/CD pipeline
- **GitHub Environments** — deployment gates and approvals

---

## What This Demonstrates

- Git branching strategy used by real engineering teams
- CI/CD pipeline design with environment promotion
- Automated testing integrated into the deployment flow
- Security-conscious configuration management (secrets never committed)
- Production deployment gates with manual approval
- Professional commit history using Conventional Commits
- Infrastructure-as-code mindset applied to pipeline design

---

*Built as a portfolio project to demonstrate DevOps and CI/CD fundamentals.*
*Pipeline architecture reflects real-world engineering team practices.*

---

## Workflows

### CI Pipeline (`ci.yml`)
Triggers on every pull request targeting `develop`, `staging`, or `main`.

Runs:
- `flake8` linting
- Full `pytest` test suite
- Health endpoint smoke test

A failing check blocks the merge. No exceptions.

### Deploy to Dev (`deploy-dev.yml`)
Triggers automatically on every push to `develop`. Loads `dev.env`,
confirms environment, logs commit SHA and actor for full auditability.

### Deploy to Staging (`deploy-staging.yml`)
Triggers automatically on merge to `staging`. Mirrors production
configuration. Runs full test suite before deployment.

### Deploy to Production (`deploy-prod.yml`)
Triggers on merge to `main`. Requires manual approval via GitHub
Environments before executing. This is the production gate.

---

## API Endpoints

| Endpoint | Method | Response |
|---|---|---|
| `/health` | GET | `{"status": "ok"}` |
| `/vitals` | GET | Heart rate, blood pressure, temperature, environment name |

The `/vitals` endpoint returns the current `environment` in its response —
making it easy to confirm the correct version is running in each environment.

---

## Quick Start

```bash
# Clone and set up
git clone https://github.com/YOUR_USERNAME/medideploy.git
cd medideploy
python3 -m venv venv
source venv/bin/activate
make install

# Run locally
make run

# Run tests
make test

# Lint
make lint
```

---

## Branch Strategy

| Branch | Purpose | Deploys to |
|---|---|---|
| `develop` | Active development | Dev environment |
| `staging` | Pre-production validation | Staging environment |
| `main` | Production-ready code | Production (with approval) |

All branches are protected. Direct pushes are blocked. Everything
goes through a pull request.

---

## Tech Stack

- **Python 3.11** + **Flask** — application
- **pytest** — testing
- **flake8** — linting
- **GitHub Actions** — CI/CD pipeline
- **GitHub Environments** — deployment gates and approvals

---

## What This Demonstrates

- Git branching strategy used by real engineering teams
- CI/CD pipeline design with environment promotion
- Automated testing integrated into the deployment flow
- Security-conscious configuration management (secrets never committed)
- Production deployment gates with manual approval
- Professional commit history using Conventional Commits
- Infrastructure-as-code mindset applied to pipeline design

---

*Built as a portfolio project to demonstrate DevOps and CI/CD fundamentals.*
*Pipeline architecture reflects real-world engineering team practices.*
