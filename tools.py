import requests
import yfinance as yf
import os
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

# Web search tool - searches internet for latest news
search_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))

def get_stock_data(ticker: str) -> dict:
    """Fetch real stock data from Yahoo Finance"""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="1mo")

        return {
            "company_name": info.get("longName", ticker),
            "current_price": info.get("currentPrice", "N/A"),
            "currency": info.get("currency", "USD"),
            "market_cap": info.get("marketCap", "N/A"),
            "52_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
            "52_week_low": info.get("fiftyTwoWeekLow", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "dividend_yield": info.get("dividendYield", "N/A"),
            "analyst_recommendation": info.get("recommendationKey", "N/A"),
            "target_price": info.get("targetMeanPrice", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
            "summary": info.get("longBusinessSummary", "N/A")[:500],
            "monthly_change": f"{((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0] * 100):.2f}%" if len(hist) > 0 else "N/A"
        }
    except Exception as e:
        return {"error": str(e)}