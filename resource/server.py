from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="resource", stateless_http=True)

docs = {
    "overview": "This project implements a minimal MCP client-server architecture for demo purposes.",
    "usage": "Run the server and use the client to interact via defined tools.",
    "api": "Refer to the MCP API schema to understand the available tools and methods.",
}


# static resource
@mcp.resource("docs://documents", mime_type="application/json")
def list_docs():
    """List of all available docs"""
    return(docs.keys())

# dynamic resource
@mcp.resource("docs://documents/{docs_name}", mime_type="application/json")
def read_docs(docs_name : str):
    """Read a specific document."""
    if docs_name in docs:
        return{"name": docs_name, "content": docs[docs_name]}
    else:
        return{"name": docs_name, "content": "Not Found Your docs"}


mcp_app = mcp.streamable_http_app()



#           run server
# uvicorn server:mcp_app --port 8001
# uvicorn server:mcp_app --reload
 