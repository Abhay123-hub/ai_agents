import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq

import phi

from phi.playground import Playground,serve_playground_app
load_dotenv()
import os
groq_api_key = os.getenv("GROQ_API_KEY")
phi.api = os.getenv("PHI_API_KEY")

## web searh agent
web_search_agent = Agent(
    name = "web search agent",
    role = "serch the web for the information",
    model = Groq(id = "gemma2-9b-it",api_key= groq_api_key),
    tools = [DuckDuckGo()],
    instruction = ["Always include the sources"],
    show_tools_calls = True,
    markdown=True
)

## financial agent
financial_agent = Agent(
    name = "Finance AI Agent",
    model = Groq(id = "gemma2-9b-it",api_key = groq_api_key),
    tools = [YFinanceTools(stock_price = True,analyst_recommendations=True,stock_fundamentals=True
            ,company_news=True)
             ],
    instructions = ["use tables to display the Data"],
    show_tool_calls = True,
    markdown = True,
    
    
)

app = Playground(agents = [financial_agent,web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload = True)