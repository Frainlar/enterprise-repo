-- Athena external tables stored as partitioned Parquet

CREATE EXTERNAL TABLE IF NOT EXISTS analytics.sap_order (
  order_id string,
  customer_id string,
  order_date date,
  total_amount double
)
PARTITIONED BY (year string, month string)
STORED AS PARQUET
LOCATION 's3://enterprise-datalake/sap_order/';

CREATE EXTERNAL TABLE IF NOT EXISTS analytics.agent_log (
  agent_id string,
  event_time timestamp,
  event_type string,
  payload string
)
PARTITIONED BY (date string)
STORED AS PARQUET
LOCATION 's3://enterprise-datalake/agent_log/';

CREATE EXTERNAL TABLE IF NOT EXISTS analytics.prompt_audit (
  prompt_id string,
  user_id string,
  created_at timestamp,
  prompt_text string
)
STORED AS PARQUET
LOCATION 's3://enterprise-datalake/prompt_audit/';
