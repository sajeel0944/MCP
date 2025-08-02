import asyncio
import json
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession, types
from contextlib import AsyncExitStack
from pydantic import AnyUrl

class MCPClient:
    def __init__(self, url):
      self.url = url
      self.stack = AsyncExitStack()
      self._sess = None
    
    async def __aenter__(self):
        read, write, _ = await self.stack.enter_async_context(
            streamablehttp_client(self.url)
        )
        self._sess = await self.stack.enter_async_context(
            ClientSession(read, write)
        )
        await self._sess.initialize()
        return self

    async def __aexit__(self, *args):
        await self.stack.aclose()

    
    async def list_resources(self) -> list[types.Resource]:
        result : types.ListResourcesResult = await self._sess.list_resources()
        return result.resources
    

    async def list_resource_templates(self) -> list[types.ResourceTemplate]:
        assert self._sess, "Session not available."
        result: types.ListResourceTemplatesResult = await self._sess.list_resource_templates()
        return result.resourceTemplates
    
    async def read_resources(self, uri: str) -> types.ReadResourceResult:
        assert self._sess, "Session not available." 
        result = await self._sess.read_resource(AnyUrl(uri))
        resource = result.contents[0]
        if isinstance(resource, types.TextResourceContents):
            if resource.mimeType == "application/json":
                try:
                    return json.loads(resource.text)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
        return resource.text
    

async def main():
    async with MCPClient("http://127.0.0.1:8000/mcp/") as client:
     
        resourse : list[types.Resource] = await client.list_resources() 
        print("\n\n✅ MCP Response: Read Resourse\n")
        print(resourse)


        template = await client.list_resource_templates()
        print("\n\n✅ MCP Response: list of resourse template \n")
        print(template)


        static_resource = await client.read_resources("docs://documents")
        print("\n\n✅ MCP Response: Static Resourse\n")
        print( static_resource)
        

        dynamic_resourse = await client.read_resources("docs://documents/api")
        print("\n\n✅ MCP Response: Dynamic Resourse\n")
        print( dynamic_resourse)

asyncio.run(main())

