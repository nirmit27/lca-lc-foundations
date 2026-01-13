"""
Setup - API + Agent mode
"""

from typing import Dict, Any

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool

from tavily import TavilyClient

from config import GEMINI_API_MODEL, GOOGLE_API_KEY


# Gemini API - LLM
gemini_model = ChatGoogleGenerativeAI(model=GEMINI_API_MODEL, api_key=GOOGLE_API_KEY)


# Tavily API - Web search tool
tavily_client = TavilyClient()


@tool(
    "web_search",
    description="Search the web for the most relevant information that can fulfill the user's request.",
)
def web_search(query: str) -> Dict[str, Any]:
    return tavily_client.search(query)


# Agent configuration

system_prompt = """
You are an intelligent personal chef agent.
The user will either give you a list of ingredients that they have left over in their house
or an image of the ingredients/contents of their refrigerator/kitchen.

Using the web search tool provided to you, search the web for recipes that can be made
with the ingredients they have.

Return recipe suggestions clearly.
If the user asks, provide full recipe instructions.
Also provide useful links when available.
"""

agent = create_agent(model=gemini_model, tools=[web_search], system_prompt=system_prompt)
