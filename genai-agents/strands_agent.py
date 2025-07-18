"""Decision making via Strands Agents."""

from __future__ import annotations

from strands_agents import StrandsEngine

from .agent_task import AgentTask


class StrandsRoutingAgent:
    """Route decisions through a Strands graph."""

    def __init__(self, config: dict | None = None) -> None:
        self.engine = StrandsEngine(config or {})

    def run(self, task: AgentTask) -> str:
        """Execute decision making with graph routing."""
        result = self.engine.route(task.description, task.context or {})
        return str(result)
