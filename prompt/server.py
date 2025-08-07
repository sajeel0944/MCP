from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP(name="prompt", stateless_http=True)


@mcp.prompt(name="greet", description="This is for greeting all", title="Hello Prompt")
def hello_greet(user_name: str) -> str:
    return f"Hello {user_name}"


@mcp.prompt()
def greet_user(user_name: str) -> list[base.UserMessage]:
    return [base.UserMessage(content=f"Hello {user_name}"), base.AssistantMessage(content="hello how i can help you")]


mcp_app = mcp.streamable_http_app()