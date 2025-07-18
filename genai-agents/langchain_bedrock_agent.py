"""LangChain agent running on AWS Bedrock."""

from __future__ import annotations

from langchain.chat_models import BedrockChat
from langchain.schema import SystemMessage

from .agent_task import AgentTask


class LangChainBedrockAgent:
    """Wrapper around a LangChain agent using Bedrock."""

    def __init__(self, model_id: str = "anthropic.claude-v2") -> None:
        self.llm = BedrockChat(model_id=model_id)

    def run(self, task: AgentTask) -> str:
        """Execute the agent task using Bedrock and return the response text."""
        messages = [SystemMessage(content=task.description)]
        resp = self.llm(messages)
        return resp.content
