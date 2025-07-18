# Data Platform

This module contains dbt models, Glue/Athena configurations, ClickHouse setup and dashboard templates.

## Contents
- **dbt/** – dbt-core project with models for SAPOrder, AgentLog and PromptAudit.
- **aws_glue_catalog.tf** – Glue database and table definitions for the S3 data lake.
- **athena/** – SQL for partitioned Parquet tables queried through Athena.
- **clickhouse/** – Docker resources for a local ClickHouse instance.
- **dashboards/** – Starter dashboards for Metabase and Superset.
