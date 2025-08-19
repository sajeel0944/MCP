from mcp.server.fastmcp import FastMCP, Context
from mcp.types import SamplingMessage, TextContent
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="session", stateless_http=False)

# MCP tool define kar rahe hain jo essay banata hai
@mcp.tool()
async def create_essay(ctx: Context, topic: str) -> str:
    try:
        print("-> server: sending 'sampling/craete'")

        # Client ko message bhej raha ho using SamplingMessage
        result = await ctx.session.create_message(
            messages=[
                SamplingMessage(
                    role="user",
                    content= TextContent(type="text", text=f"write a eassy: {topic}")
                ),
            ],
            max_tokens=100,
        )

        # Agar content ka type "text" hai to usay wapas return karo
        if result.content.type == "text":
            return result.content.text
        
        # Agar koi aur type hai to usay string bana kar return karo
        return str(result.content)

    except Exception as e:
        print(f"-> Server: An error occurred during sampling: {e}")
        return f"Error asking client to generate story: {e}"
    
mcp_app = mcp.streamable_http_app()