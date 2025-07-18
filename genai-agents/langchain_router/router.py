from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

from langchain.chat_models import ChatOpenAI
from langchain.chains.router import MultiPromptChain
from langchain.prompts import PromptTemplate

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.planning.sequential_planner import SequentialPlanner

from ..agent_task import AgentTask


class LangChainRouter:
    """Route tasks using LangChain with Semantic Kernel fallback."""

    def __init__(
        self,
        promptflow_path: str | Path,
        skills: Iterable[str] | None = None,
        model: str = "gpt-3.5-turbo",
    ) -> None:
        self.prompt_template = self._load_promptflow(promptflow_path)
        self.llm = ChatOpenAI(model=model)
        self.kernel = self._init_kernel(model)
        if skills:
            for skill in skills:
                self.kernel.import_semantic_skill_from_directory(Path(skill))
        self.planner = SequentialPlanner(self.kernel)

    def _init_kernel(self, model: str) -> sk.Kernel:
        kernel = sk.Kernel()
        kernel.add_chat_service("chat", OpenAIChatCompletion(model=model))
        return kernel

    @staticmethod
    def _load_promptflow(path: str | Path) -> PromptTemplate:
        data = json.loads(Path(path).read_text())
        template = data.get("prompt", "{input}")
        input_vars = data.get("input_variables", ["input"])
        return PromptTemplate(template=template, input_variables=input_vars)

    def run(self, task: AgentTask) -> str:
        """Route the task using LangChain or fallback to Semantic Kernel."""
        context = task.context or {}
        prompt = self.prompt_template
        try:
            chain = MultiPromptChain.from_prompts(self.llm, [prompt])
            result = chain.run({**context, "input": task.description})
            if result:
                return result
        except Exception:
            pass
        # LangChain failed or returned empty, use Semantic Kernel planner
        plan = self.planner.create_plan(task.description)
        sk_result = self.kernel.invoke_sync(plan, input=context)
        return str(sk_result)
