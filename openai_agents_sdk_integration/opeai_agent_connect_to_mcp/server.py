from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Make tool", stateless_http=True)


# read docs
@mcp.tool(name="Greeting",description="This is greeting tool")
def greeting(name: str) -> str:
    print(f"Hello {name} Thsi is greeting tool cell")
    return f"Hello {name} how are you"

@mcp.tool(name="mood",description="rerturn user mood from the shared MCP server")
def mood(name: str) -> str:
    print(f"Tool 'mood' called with name: {name}")
    return "I am happy"

mcp_app = mcp.streamable_http_app()


#           run server
# uvicorn server:mcp_app --reload
 
