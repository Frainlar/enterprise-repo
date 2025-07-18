from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class AgentTask:
    """Simple container for a task given to an agent."""

    description: str
    context: Dict[str, Any] | None = None
