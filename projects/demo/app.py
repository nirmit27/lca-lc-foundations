"""
Demo Script

— Simple weather agent.
"""

from langchain.agents import create_agent
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    # TODO: integrate real API
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="ollama:gemma4:31b-cloud",
    tools=[get_weather],
    system_prompt="You are a helpful reactive assistant.",
    checkpointer=InMemorySaver(),
)

config: RunnableConfig = {"configurable": {"thread_id": "demo-1"}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in Lucknow?"}]},
    config=config,
)

for msg in result["messages"]:
    msg.pretty_print()
