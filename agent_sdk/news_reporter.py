from agents import Agent, Runner
from agents import WebSearchTool
from dotenv import load_dotenv
import os
import asyncio


async def main():

    load_dotenv()

    api_key = os.getenv("OPEN_AI_API")

    news_agent = Agent(
        name="News Search Agent",
        instructions="You are a news search agent. You'll be given a query and your job is to find the latest news articles related to that query.",
        model="gpt-4o-mini",
        tools=[WebSearchTool()],
    )

    while True:
        query = input("Enter your news query (or 'quit' to quit): ")
        if query.lower() == "quit":
            break
        result = await Runner.run(news_agent, query)
        print(result.final_output)
        print("\n" + 50 * "-", "\n")


asyncio.run(main())
