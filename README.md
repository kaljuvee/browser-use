# Browser-Use

A Python package for browser automation using LangChain and Playwright.

## Quick Start

### Installation

Install using pip:
```bash
pip install -r requirements.txt
```

Install Playwright:
```bash
playwright install
```

### Basic Usage

```python
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
```

### Running it
```bash
python main.py
```

## Dependencies

- langchain-openai
- browser-use
- asyncio
- python-dotenv
- playwright
## Requirements

- Python 3.7+
- OpenAI API key (set in environment variables)
- Playwright browser automation framework