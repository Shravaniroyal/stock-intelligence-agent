from crewai import Task
from agents import stock_data_agent, news_agent, sentiment_agent, report_agent

research_task = Task(
    description="Search for '{ticker}' stock: current price, market cap, PE ratio, 52-week high/low, analyst target price. One search only. Be concise.",
    expected_output="Stock metrics in 5 bullet points maximum.",
    agent=stock_data_agent
)

news_task = Task(
    description="Search for top 3 recent news about '{ticker}' stock from last 30 days. One search only. Be brief.",
    expected_output="3 news items with one line impact each.",
    agent=news_agent
)

sentiment_task = Task(
    description="Search Reddit sentiment for '{ticker}' stock. One search only. Is it Bullish, Bearish or Neutral?",
    expected_output="One paragraph: overall sentiment and top investor concern.",
    agent=sentiment_agent
)

report_task = Task(
    description="""Write a short professional stock report for '{ticker}' using the research, news and sentiment gathered.

Include:
1. COMPANY SNAPSHOT - 2 lines
2. KEY METRICS - from research
3. NEWS IMPACT - 3 bullets
4. SENTIMENT - one line
5. 30-DAY PREDICTION:
   📈 FORECAST: [BULLISH/BEARISH/NEUTRAL]
   🎯 Price Range: $X - $Y
   📊 Confidence: X%
   💡 Reason: one sentence
6. VERDICT: BUY / HOLD / SELL

Keep entire report under 400 words.""",
    expected_output="Complete stock report under 400 words with prediction and verdict.",
    agent=report_agent,
    output_file="stock_report.md"
)