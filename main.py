from crewai import Crew
from agents import stock_data_agent, news_agent, sentiment_agent, report_agent
from tasks import research_task, news_task, sentiment_task, report_task
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def find_ticker(company_name: str) -> str:
    """
    Searches Yahoo Finance to find the correct ticker symbol
    for ANY company worldwide — including subsidiaries.
    """
    try:
        url = f"https://query2.finance.yahoo.com/v1/finance/search?q={company_name}&quotesCount=10&newsCount=0"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()
        
        quotes = data.get("quotes", [])
        
        # Filter only stocks (not ETFs, crypto etc)
        stocks = [q for q in quotes if q.get("quoteType") == "EQUITY"]
        
        if not stocks:
            print(f"\n⚠️  No stocks found for '{company_name}'. Try a ticker directly (e.g. NVDA, TCS.NS)")
            return input("Enter ticker manually: ").upper()
        
        if len(stocks) == 1:
            ticker = stocks[0]["symbol"]
            name = stocks[0].get("longname") or stocks[0].get("shortname", ticker)
            print(f"\n✅ Found: {name} [{ticker}]")
            confirm = input("Is this correct? (y/n): ").strip().lower()
            if confirm == "y":
                return ticker
            else:
                return input("Enter ticker manually: ").upper()
        
        # Multiple results — show options
        print(f"\n🔍 Found multiple companies matching '{company_name}':")
        print("-" * 60)
        for i, stock in enumerate(stocks[:8], 1):
            name = stock.get("longname") or stock.get("shortname", "Unknown")
            ticker = stock["symbol"]
            exchange = stock.get("exchange", "")
            sector = stock.get("sector", "")
            print(f"  {i}. {name}")
            print(f"     Ticker: {ticker} | Exchange: {exchange}")
            if sector:
                print(f"     Sector: {sector}")
            print()
        
        choice = input(f"Enter number (1-{min(len(stocks), 8)}) or type ticker manually: ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= min(len(stocks), 8):
            selected = stocks[int(choice) - 1]
            ticker = selected["symbol"]
            name = selected.get("longname") or selected.get("shortname", ticker)
            print(f"\n✅ Selected: {name} [{ticker}]")
            return ticker
        else:
            return choice.upper()
            
    except Exception as e:
        print(f"\n⚠️  Search failed: {e}")
        return input("Enter ticker manually: ").upper()


def analyze_stock(ticker: str):
    print(f"\n🚀 Starting AI Stock Analysis for: {ticker}")
    print("=" * 60)

    crew = Crew(
        agents=[stock_data_agent, news_agent, sentiment_agent, report_agent],
        tasks=[research_task, news_task, sentiment_task, report_task],
        verbose=True
    )

    result = crew.kickoff(inputs={"ticker": ticker})

    print("\n" + "=" * 60)
    print("✅ ANALYSIS COMPLETE!")
    print("📄 Full report saved to: stock_report.md")
    print("=" * 60)
    print(result)


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("   🤖 AI STOCK INTELLIGENCE SYSTEM")
    print("   Covers stocks worldwide — NYSE, NASDAQ, NSE, BSE & more")
    print("=" * 60)
    
    user_input = input("\n🔎 Enter company name or ticker (e.g. 'Infosys', 'Jio', 'NVDA', 'Tata Steel'): ").strip()
    
    # Check if it looks like a ticker already (short, uppercase)
    if len(user_input) <= 6 and user_input.replace(".", "").replace("-", "").isupper():
        ticker = user_input.upper()
        print(f"\n✅ Using ticker: {ticker}")
    else:
        ticker = find_ticker(user_input)
    
    analyze_stock(ticker)