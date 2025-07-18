"""Knowledge graph integration using LlamaGraph."""

from __future__ import annotations

from llamagraph import Graph

from .agent_task import AgentTask


class LlamaGraphAgent:
    """Queries a knowledge graph via LlamaGraph."""

    def __init__(self, uri: str) -> None:
        self.graph = Graph(uri)

    def run(self, task: AgentTask) -> str:
        """Run a graph query based on the task description."""
        result = self.graph.query(task.description)
        return str(result)
