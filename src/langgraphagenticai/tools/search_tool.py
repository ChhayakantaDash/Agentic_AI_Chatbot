from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tavily_tool = TavilySearchResults(max_results=2)
    tavily_tool.name = "news_search_json"   # Force the tool to match what LLM expects
    return [tavily_tool]

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)
