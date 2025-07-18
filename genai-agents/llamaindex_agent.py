"""Context aware retrieval using LlamaIndex."""

from __future__ import annotations

from llama_index import VectorStoreIndex, SimpleDirectoryReader

from .agent_task import AgentTask


class LlamaIndexAgent:
    """Uses LlamaIndex to provide RAG functionality."""

    def __init__(self, data_path: str) -> None:
        documents = SimpleDirectoryReader(data_path).load_data()
        self.index = VectorStoreIndex.from_documents(documents)
        self.query_engine = self.index.as_query_engine()

    def run(self, task: AgentTask) -> str:
        """Query the index with the task description."""
        response = self.query_engine.query(task.description)
        return str(response)
