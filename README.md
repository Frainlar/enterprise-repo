# Enterprise Monorepo

This repository provides a boilerplate for a scalable AI‑native application platform. It uses **Turborepo** to manage polyglot microservices and shared packages.

## Structure

- **apps/** – web, mobile and backend services
- **genai-agents/** – multi‑agent orchestration
- **vector-stores/** – vector databases and embeddings
- **data-platform/** – lakehouse and analytics
- **sap-integration/** – SAP connectivity helpers
- **packages/** – reusable libraries
- **infra/** – infrastructure as code
- **tests/** – end‑to‑end tests

Each service is intentionally minimal. Extend the modules as needed for your organisation.
