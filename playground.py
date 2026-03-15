#Lets visualize the same agent with an UI
print("Script started...")

from dotenv import load_dotenv
load_dotenv()

from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
import openai
from phi.agent import Agent
import phi.api
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import phi
from phi.playground import Playground, serve_playground_app


phi.api=os.getenv("PHI_API_KEY")

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

app = Playground(agents=[financial_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)
