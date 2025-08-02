from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="server and client", stateless_http=True)

@mcp.tool(name="weather", description="Weather information")
def weather(name: str) -> str:
    return f"weather is {name}"

mcp_app = mcp.streamable_http_app()

# #           run server
# # uvicorn server:mcp_app --port 8001
# # uvicorn server:mcp_app --reload