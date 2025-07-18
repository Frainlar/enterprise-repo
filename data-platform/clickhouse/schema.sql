CREATE TABLE IF NOT EXISTS sap_order (
    order_id String,
    customer_id String,
    order_date Date,
    total_amount Float64
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(order_date)
ORDER BY (order_id);

CREATE TABLE IF NOT EXISTS agent_log (
    agent_id String,
    event_time DateTime,
    event_type String,
    payload String
) ENGINE = MergeTree()
PARTITION BY toDate(event_time)
ORDER BY (agent_id, event_time);

CREATE TABLE IF NOT EXISTS prompt_audit (
    prompt_id String,
    user_id String,
    created_at DateTime,
    prompt_text String
) ENGINE = MergeTree()
ORDER BY (prompt_id);
