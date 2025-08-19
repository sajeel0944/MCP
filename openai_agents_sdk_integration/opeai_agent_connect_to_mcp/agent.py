from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, enable_verbose_stdout_logging, set_tracing_disabled
from agents.run import RunConfig
from agents.mcp import MCPServerStreamableHttp, MCPServerStreamableHttpParams
import asyncio
from dotenv import load_dotenv
import os


#----------------------------------------------------------------

load_dotenv()
set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

#----------------------------------------------------------------

GEMINI_API_KEY : str = os.getenv("GEMINI_API_KEY")
MODEL : str = "gemini-2.5-flash"

#----------------------------------------------------------------

external_client = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = MODEL,
    openai_client = external_client 
)

config = RunConfig(
    model = model,
    model_provider = external_client ,
    tracing_disabled = True
)

async def main():
    params_config = MCPServerStreamableHttpParams(url="http://localhost:8000/mcp/")
    async with MCPServerStreamableHttp(params=params_config, name="HelloMCPAGI") as mcp_server:

        agent = Agent(
            name="Bank Assistant",
            instructions="You are a helpful assistant. Use user_all_deatils tool to show user info.",
            model=model,
            mcp_servers=[mcp_server]
        )

        response = await Runner.run(agent, "what is my mood sajeel")

        print(response.final_output)

if __name__ in "__main__":
    asyncio.run(main())