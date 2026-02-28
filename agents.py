from crewai import Agent, LLM
from tools import search_tool
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="mistral/mistral-small-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

stock_data_agent = Agent(
    role="Stock Data Specialist",
    goal="Search for stock price and key metrics for the given ticker symbol",
    backstory="You are a stock market expert. Search once and give concise data.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    max_iter=2
)

news_agent = Agent(
    role="Financial News Analyst",
    goal="Find top 3 recent news items for the given stock",
    backstory="You find the most important recent news affecting a stock. Be brief.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    max_iter=2
)

sentiment_agent = Agent(
    role="Sentiment Analyst",
    goal="Find overall investor sentiment for the stock",
    backstory="You check Reddit and finance sites for investor mood. One search only.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    max_iter=2
)

report_agent = Agent(
    role="Investment Report Writer",
    goal="Write a concise stock report with 30-day price prediction",
    backstory="You write short professional investment reports with clear BUY/HOLD/SELL verdicts.",
    llm=llm,
    verbose=True,
    max_iter=2
)