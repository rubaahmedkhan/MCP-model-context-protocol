from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="hello_mcp", stateless_http=True)

@mcp.tool(name="online_researcher", description="search the web for information")
def search_online(query: str) -> str:
    return f'Results for {query}...'

@mcp.tool()
async def get_weather(city: str) -> str:
    return f"Weather in {city} is sunny."


mcp_app = mcp.streamable_http_app()

