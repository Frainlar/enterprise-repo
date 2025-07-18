# Enterprise Monorepo

This repository provides a boilerplate for a scalable AI‑native application platform. It uses an **Nx workspace** to manage polyglot microservices and shared packages.

## Folder Overview

- **apps/frontend** – Next.js App Router with Tailwind CSS, ShadCN UI and DaisyUI.
- **apps/mobile** – Flutter project with PWA support generated via PWABuilder.
- **apps/nest-core-api** – Nest.js API running on the Bun runtime and using Prisma ORM.
- **apps/actix-core-api** – Rust microservice built with Actix Web.
- **apps/gin-analytics-api** – Go service using the Gin framework for analytics features.
- **apps/fastapi-report-engine** – FastAPI based reporting engine with Prisma client.
- **genai-agents** – LangChain, CrewAI and AutoGen examples for multi‑agent orchestration.
- **vector-stores** – MongoDB Atlas and S3 clients for managing vector embeddings.
- **data-platform** – dbt models, Glue Catalog/Athena queries, ClickHouse schemas and dashboards.
- **sap-integration** – OData helpers and SAP BTP Destination configurations.
- **packages** – Shared libraries such as auth-lib, utilities and the Prisma client.
- **infra** – Terraform modules, Dockerfiles, Kubernetes manifests and observability tooling.
- **tests** – Playwright end‑to‑end test suite.

Each service is intentionally minimal. Extend the modules as needed for your organisation.
