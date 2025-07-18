"""Simple control plane to orchestrate agents."""

from __future__ import annotations

from typing import Iterable

from genai_agents import AgentTask


class MultiAgentController:
    """Dispatch tasks to multiple agents and gather results."""

    def __init__(self, agents: Iterable) -> None:
        self.agents = list(agents)

    def run(self, task: AgentTask) -> list[str]:
        """Run the task across all registered agents."""
        results = []
        for agent in self.agents:
            if hasattr(agent, "run"):
                results.append(agent.run(task))
        return results
