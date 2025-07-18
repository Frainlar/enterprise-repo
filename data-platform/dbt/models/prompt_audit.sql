select
  prompt_id,
  user_id,
  created_at,
  prompt_text
from {{ source('audit', 'prompts') }}
