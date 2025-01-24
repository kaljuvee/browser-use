from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def main():
    # Initialize agent
    agent = Agent(
        task="Go to Reddit, search for 'browser-use' in the search bar, click on the first post",
        llm=ChatOpenAI(model="gpt-4o-mini")
    )
    
    # Run the agent
    result = await agent.run()
    print(result)

# Run the async main function
asyncio.run(main())