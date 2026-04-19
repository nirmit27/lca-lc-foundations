"""
MCP Server : Docs

- A sample LOCAL MCP server script for fetching the available documentation on LangChain, LangGraph and LangSmith.
"""

from requests import get
from typing import Dict, Any
from dotenv import load_dotenv

from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient

load_dotenv()

mcp = FastMCP("github_docs_fetcher")
tavily_client = TavilyClient()


# NOTE: Tool for searching the web
@mcp.tool(name="search_web", description="Search the web for accurate information.")
def search_web(query: str) -> Dict[str, Any]:
    results = tavily_client.search(query)
    return results


# NOTE: Resources - provide access to langchain-ai repo files
@mcp.resource(
    name="github_file",
    uri="github://langchain-ai/langchain-mcp-adapters/blob/main/README.md",
    description="Resource for accessing the langchain-ai/langchain-mcp-adapters/README.md file.",
)
def github_file():
    url = f"https://raw.githubusercontent.com/langchain-ai/langchain-mcp-adapters/blob/main/README.md"
    try:
        resp = get(url)
        return resp.text
    except Exception as e:
        return f"Error: {str(e)}"


# NOTE: Prompt template
@mcp.prompt(
    name="prompt",
    description="Analyze data from a langchain-ai repo file with comprehensive insights",
)
def prompt():
    return """
    You are a helpful assistant that answers user questions about LangChain, LangGraph and LangSmith.

    You can use the following tools/resources to answer user questions:
    - search_web: Search the web for latest available information.
    - github_file: Access the langchain-ai repo files for obtaining information from the official GitHub repo.

    Rules to be taken into consideration while responding to user queries:
    1. If the user asks a question that is not related to LangChain, LangGraph or LangSmith, you should say "Sorry, I can only answer questions related to LangChain, LangGraph and LangSmith."
    2. You may try multiple tool and resource calls to respond to the user's query.
    3. You may also ask clarifying questions to the user to get a better understanding of their query.
    """


if __name__ == "__main__":
    mcp.run(transport="stdio")
