import asyncio

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.server import Context
from mcp import types

mcp = FastMCP(
    name="Simple Logging Server",
    stateless_http=True  
)

# Tool define kiya gaya jo client call karega
@mcp.tool(
    name="process_item",
    description="Processes an item and generates logs at different levels."
)
async def process_item(
    ctx: Context, # Tool ka context (logs send karne ke liye)
    item_id: str, # Client se aane wala item ID 
    should_fail: bool = False, # agar ye True howa to error show hoye ga
) -> list[types.TextContent]:
    """
    A simple tool that demonstrates logging by emitting messages
    at different severity levels.
    """
    await ctx.debug(f"Starting processing for item: {item_id}") # Debug level log: item process karna start
    await asyncio.sleep(0.2)
    await ctx.info("Configuration loaded successfully.") # Info level log: config load ho gayi
    await asyncio.sleep(0.2)

    if should_fail: # agar should_fail True ho wa to ye show hoye ga
        await ctx.warning(f"Item '{item_id}' has a validation issue. Attempting to proceed...")
        await asyncio.sleep(0.2)
        await ctx.error(f"Failed to process item '{item_id}'. Critical failure.") # Error log
        return [types.TextContent(type="text", text=f"Failed to process {item_id}.")] # Failure message return karo

    await ctx.info(f"Item '{item_id}' processed successfully.") # Success message log karo

    return [types.TextContent(type="text", text=f"Successfully processed {item_id}.")] # Success message return karo

# Create the streamable HTTP app for stateful connections
mcp_app = mcp.streamable_http_app()