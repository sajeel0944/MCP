from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="online_class", stateless_http=True)

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# read docs
@mcp.tool()
def read_docs(docs_id: str) -> str:
    return docs.get(docs_id, "Not find your docs")

# edit docs
@mcp.tool()
def edit_docs(docs_id: str, new_docs: str) -> bool:
    docs[docs_id] = new_docs
    return True

mcp_app = mcp.streamable_http_app()


#           run server
# uvicorn server:mcp_app --port 8001
 