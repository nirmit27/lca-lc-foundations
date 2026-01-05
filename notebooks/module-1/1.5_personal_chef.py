"""
Sample agent - Personal Chef
"""

from dotenv import load_dotenv

from langchain.tools import tool
from langchain.agents import create_agent

from tavily import TavilyClient

load_dotenv()
tavily_client = TavilyClient()


@tool
def web_search(query):
    """Surf the web for any relevant information"""
    return tavily_client.search(query)


system_prompt = """You are a personal chef. The user will give you a list of ingredients they have left over in their house.
Using the web search tool, search the web for recipes that can be made with the ingredients they have.
Return recipe suggestions and eventually the recipe instructions to the user, if requested.
"""


agent = create_agent(
    model="gpt-5-nano", tools=[web_search], system_prompt=system_prompt
)
