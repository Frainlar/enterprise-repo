FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV AGENT_MODULE=autogen_agent
CMD ["python", "-m", "genai_agents.${AGENT_MODULE}"]
