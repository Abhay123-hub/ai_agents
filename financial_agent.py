from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools ## finane related information
from phi.tools.duckduckgo import DuckDuckGo ## for web search

import os
groq_api_key = os.getenv("GROQ_API_KEY")
from dotenv import load_dotenv
load_dotenv()


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

multi_ai_agent = Agent(
    team = [web_search_agent,financial_agent],
    instructions = ["Always include sources","use table to show tha data"],
    show_tool_calls= True,
    markdown = True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream = True)
