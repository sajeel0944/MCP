#                   part 1

print("\n\n\n\t\t\t\t\t part 1 \n\n\n")

import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession, types

# MCP server URL
url = "http://127.0.0.1:8001/mcp/"

async def main():
    # Use async context manager properly and unpack the returned values
    async with streamablehttp_client(url) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            result_1 = await session.list_tools()
            print("\n\n✅ MCP Response: Read All Tool Schema\n")
            print(result_1)


            result_2 = await session.call_tool(
                name="read_docs",
                arguments={"docs_id": "plan.md"}
            )
            print("\n\n✅ MCP Response: Read Docs\n")
            print(result_2)

            result_3 = await session.call_tool(
                name="edit_docs",
                arguments={"docs_id": "plan.md", "new_docs": "The implementation strategy for the project is laid out in this plan."}
            )
            print("\n\n✅ MCP Response: Edit Docs \n")
            print(result_3)
        
# Run it
asyncio.run(main())


# -----------------------------------------------part 2--------------------------------------------------------------


print("\n\n\n\t\t\t\t\t part 2 \n\n\n")

import requests

url = "http://127.0.0.1:8001/mcp/"

header = {
    "Accept": "application/json, text/event-stream"
}

body_1 : list = {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "params": {},
    "id": 1
}

response_1 = requests.post(url, headers=header, json=body_1)
print("\n\n✅ MCP Response: Read All Tool Schema\n")
print(response_1.text)



body_2 = {
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "read_docs",
    "arguments": {
      "docs_id": "plan.md"
    }
  }
}

response_2 = requests.post(url, headers=header, json=body_2)
print("\n\n✅ MCP Response: Read Docs\n")
print(response_2.text)



body_3 = {
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "edit_docs",
    "arguments": {
      "docs_id": "plan.md",
      "new_docs": "The implementation strategy for the project is laid out in this plan."
    }
  }
}

response_3 = requests.post(url, headers=header, json=body_3)
print("\n\n✅ MCP Response: Edit Docs\n")
print(response_3.text)