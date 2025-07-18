# GenAI Agents

This folder contains orchestrators for various generative AI frameworks. Each agent exposes a standard `run(task: AgentTask)` interface.

- **LangChainBedrockAgent** – LangChain agent running on AWS Bedrock
- **CrewAgent** – role and task decomposition with CrewAI
- **AutoGenOrchestrator** – multi-agent dialogue using AutoGen
- **LlamaIndexAgent** – context-aware retrieval augmented generation
- **LlamaGraphAgent** – knowledge graph querying via LlamaGraph
- **StrandsRoutingAgent** – graph-routed decision making
