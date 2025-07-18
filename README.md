# Enterprise Monorepo

This repository provides a boilerplate for a scalable AI‑native application platform. It uses an **Nx workspace** to manage polyglot microservices and shared packages. See [architecture.md](architecture.md) for an overview of the data and control flow.

## Repository Structure

### Applications
- **apps/frontend** – Next.js App Router with Tailwind CSS, ShadCN UI and DaisyUI.
- **apps/mobile** – Flutter project with PWA support generated via PWABuilder.
- **apps/nest-core-api** – Nest.js API running on the Bun runtime and using Prisma ORM.
- **apps/actix-core-api** – Rust microservice built with Actix Web.
- **apps/gin-analytics-api** – Go service using the Gin framework for analytics features.
- **apps/fastapi-report-engine** – FastAPI based reporting engine with Prisma client.
- **apps/docs** – Astro site containing developer and product documentation.

### Agents and Control Plane
- **genai-agents** – LangChain, CrewAI, AutoGen and other agent implementations.
- **a2a-protocol** – utilities for agent‑to‑agent messaging.
- **mcp-controller** – dispatches `AgentTask` objects to multiple agents and aggregates the results.

### Data and Integrations
- **vector-stores** – MongoDB Atlas and S3 clients for managing vector embeddings.
- **sap-integration** – OData helpers and SAP BTP Destination configurations.
- **data-platform** – dbt models, Glue Catalog/Athena queries, ClickHouse schemas and dashboards.

### Shared Packages
- **packages/prisma-client** – generated Prisma client library.
- **packages/realtime** – Fluid Framework helpers backed by Redis.
- **packages/shared-ui** – React component library used by the frontend and docs.
- **packages/utils** – general utilities shared across services.

### Infrastructure and Tests
- **infra** – Terraform modules, Dockerfiles, Kubernetes manifests and observability tooling.
- **tests** – Playwright end‑to‑end and visual test suite.
- **storybook** – configuration for UI component development.

Each service is intentionally minimal. Extend the modules as needed for your organisation.

## Agents

The `genai-agents` folder contains orchestrators used by the control plane:

- **LangChainBedrockAgent** – wraps a LangChain agent running on AWS Bedrock.
- **CrewAgent** – breaks down tasks by role using CrewAI.
- **AutoGenOrchestrator** – multi‑agent dialogue orchestrated with AutoGen.
- **LlamaIndexAgent** – retrieval‑augmented generation via LlamaIndex.
- **LlamaGraphAgent** – knowledge graph querying powered by LlamaGraph.
- **StrandsRoutingAgent** – decision making using Strands Agents.
- **LangChainRouter** – routes tasks with Promptflow templates and Semantic Kernel.
- **RedisStateStore** – persists agent state, chat context and collaborative docs.

The `MultiAgentController` in `mcp-controller` dispatches a task to any combination of these agents.

## Local Development

1. Install Node.js 20+ and run `corepack enable` to activate pnpm.
2. Install dependencies: `pnpm install`.
3. Start all apps for development: `pnpm dev`.
4. For the documentation site: `cd apps/docs && pnpm dev`.
5. Python agents require `pip install -r genai-agents/requirements.txt`.

## Cloud Deployment

1. Provision infrastructure using the Terraform modules in `infra/`.
2. Build container images from each application's Dockerfile and push them to your registry.
3. Deploy the images to Kubernetes (manifests are provided in `infra/`).
4. Configure environment variables for SAP access, vector stores and Redis as described in the respective READMEs.
5. Run `dbt` and apply the dashboards under `data-platform` to set up analytics.

## CI/CD

- **ci.yml** – installs dependencies, lints, builds, and runs Playwright tests on pushes and pull requests. Successful runs on `main` trigger deployment.
- **designops.yml** – builds Storybook and executes Lost Pixel visual regression tests when UI packages change.

## Real-time Collaboration

- Elasticache for Redis is provisioned via Terraform and acts as the coordination layer for pub/sub.
- The `@enterprise/realtime` package uses Fluid Framework to sync data in real time across the Next.js frontend and Flutter mobile app.
- Example usage is provided as a shared task list where updates are stored in Redis along with agent state, chat context and collaborative docs.

Refer to [architecture.md](architecture.md) for the full platform diagram.
