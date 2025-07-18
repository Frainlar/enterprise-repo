"""Redis-backed agent state and chat context storage."""

from __future__ import annotations

import json
from typing import Any, Dict, Optional
import redis


class RedisStateStore:
    def __init__(self, url: str) -> None:
        self.client = redis.Redis.from_url(url)

    def save_agent_state(self, agent_id: str, state: Dict[str, Any]) -> None:
        self.client.hset("agent_state", agent_id, json.dumps(state))

    def load_agent_state(self, agent_id: str) -> Optional[Dict[str, Any]]:
        data = self.client.hget("agent_state", agent_id)
        return json.loads(data) if data else None

    def append_chat_context(self, session_id: str, message: str) -> None:
        self.client.rpush(f"chat:{session_id}", message)

    def get_chat_context(self, session_id: str) -> list[str]:
        messages = self.client.lrange(f"chat:{session_id}", 0, -1)
        return [m.decode() for m in messages]

    def save_document(self, doc_id: str, content: str) -> None:
        self.client.set(f"doc:{doc_id}", content)

    def load_document(self, doc_id: str) -> Optional[str]:
        data = self.client.get(f"doc:{doc_id}")
        return data.decode() if data else None
