#This is a combiation of agents and they all together will be able to do multiple tasks and give me the results. 
#The first agent will be doing all the interaction to get the details of teh stock
#Then another agent will be able to collect all the news from a web browser
print("Script started...")

from dotenv import load_dotenv
load_dotenv()

print("Script started...")
from phi.agent import Agent
print("Script started...")
from phi.tools.duckduckgo import DuckDuckGo
print("Script started...")
from phi.model.groq import Groq
print("Script started...")
from phi.tools.yfinance import YFinanceTools

import openai

import os
openai.api_key=os.getenv("OPENAI_API_KEY")

print("All imports successfull")

## websearch agent -- Agent 1
web_search_agent=Agent(
    name = "Web Search Agent",
    role = "Search the Web for the Information",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls = True,
    markdown = True,

)

## Financial Agent -- Agent 2

financial_agent =  Agent (
    name = "Finance AI Agent",
    role = "Search Stock Details",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True, 
                           analyst_recommendations=True, 
                           stock_fundamentals=True,
                           company_news=True)],
    instructions = ["Use Tables to display the data"],
    show_tool_calls =  True,
    markdown = True,
)

multi_ai_agent = Agent(
    team = [web_search_agent,financial_agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions =  ["Always include sources","use table to display the data"],
    show_tool_calls = True,
    markdown = True
)

multi_ai_agent.print_response("Summerize analyst recommendations and share the latest news for NVDA", stream = True)