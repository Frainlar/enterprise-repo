"""AutoGen multi-agent dialogue orchestrator."""

from __future__ import annotations

from autogen.agentchat import Agent

from .agent_task import AgentTask


class AutoGenOrchestrator:
    """Orchestrates a dialogue between agents using AutoGen."""

    def __init__(self, agents: list[Agent] | None = None) -> None:
        self.agents = agents or []

    def run(self, task: AgentTask) -> str:
        """Start a dialogue using the provided agents and return the final output."""
        if not self.agents:
            return "No agents configured"
        message = task.description
        for agent in self.agents:
            message = agent.generate_reply(message)
        return message
