select
  agent_id,
  event_time,
  event_type,
  payload
from {{ source('logs', 'agent_events') }}
