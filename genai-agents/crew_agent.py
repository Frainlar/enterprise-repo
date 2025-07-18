"""CrewAI based task decomposition."""

from __future__ import annotations

from crewai import Crew, Task

from .agent_task import AgentTask


class CrewAgent:
    """Uses CrewAI to break down tasks by role."""

    def __init__(self, role: str = "assistant") -> None:
        self.role = role

    def run(self, task: AgentTask) -> str:
        """Decompose the task using CrewAI and return combined result."""
        crew = Crew(role=self.role)
        crew_task = Task(description=task.description, context=task.context or {})
        result = crew.execute([crew_task])
        return result
