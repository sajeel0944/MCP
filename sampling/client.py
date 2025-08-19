import asyncio
from typing import Any
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.types import CreateMessageRequestParams, CreateMessageResult, ErrorData, TextContent
from mcp.shared.context import RequestContext
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, AsyncOpenAI
from agents.run import RunConfig
from dotenv import load_dotenv
import os

#----------------------------------------------------------------------------

set_tracing_disabled(disabled=True)
load_dotenv()

#----------------------------------------------------------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/"  

#----------------------------------------------------------------------------

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client,
)

run_config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

# Yeh function server se request receive karne ke liye hai context ky andar Request ka context aye ga  params ky andar Request parameters aye ga
async def mock_sampler(context: RequestContext["ClientSession", Any], params: CreateMessageRequestParams) -> CreateMessageRequestParams | ErrorData:
    try:
        print("<- Client: Received 'sampling/create' request from server.")

        print(f"<- Client Parameters '{params}'.")
        print(f"<- Client Context '{context}'.")
        print(f"<- Client Message '{params.messages}'.")

        # Messages ko aise convert karna ke model samajh sake
        converted_messages = [
            {"role": message.role, "content": message.content.text}
            for message in params.messages
        ]

        mock_agent = Agent(
            name="Assistant",
            instructions="You assistant you make only essay any topic",
            model=model
        )

        response = await Runner.run(mock_agent, converted_messages)

        print("-> Client: Sending mock eassy back to the server.")

        # Server ko response send karna
        return CreateMessageResult(
            role="assistant",
            content=TextContent(type="text", text=response.final_output),
            model="gemini-1.5-flash"
        )
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("💡 Make sure the server is running.")

# Main function jo server se connect kar ke essay ka tool cell kar raha hai
async def main():
    server_url : str = "http://localhost:8000/mcp/"
    print(f"🚀 Connecting to MCP server at {server_url}")
    try:
        # Streamable HTTP client ke sath connection establish kar raha ho
        async with streamablehttp_client(server_url) as (read_stream, write_stream, get_session_id):
            async with ClientSession(read_stream, write_stream, sampling_callback=mock_sampler) as session:
                print("✅ Connected. Initializing session...")
                await session.initialize() # Session initialize ho raha hai
                print("🛠️ Session initialized.")

                # ye prompy server ky pass jaye ga waha sy 
                story_topic = "write a  essay in plant important in the word 100 word"
                print(f"-> Client: Calling 'create_essay' tool with topic: '{story_topic}'")

                # Tool call kar raha ho mock_sampler ky andar ho agent hai us ky pass jaye ga 
                tool_result = await session.call_tool("create_essay", {"topic": story_topic})

                print("-" * 50)
                print(f"🎉 Final Story Received from Server: {tool_result}")
                if tool_result:
                    print(f"'5trrr535 {tool_result.content[0].text}'")
                else:
                    print("No content received from server.")

                print("\n✅ Demo complete!")

    except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("💡 Make sure the server is running.")


if __name__ == "__main__":
    asyncio.run(main())
