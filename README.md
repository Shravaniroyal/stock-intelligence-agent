# 🤖 AI Stock Intelligence System

> A multi-agent AI system that analyzes any stock worldwide and delivers professional investment reports with 30-day price predictions.

---

## 🎯 What It Does

You type a company name (like "Tata", "Infosys", "NVDA") → 4 AI agents work together → you get a full investment report with a **BUY / HOLD / SELL** verdict.

```
Enter company name: Tata

🔍 Found multiple companies matching 'Tata':
  1. Tata Communications   [TATACOMM.NS]
  2. Tata Consultancy Services  [TCS.NS]
  3. Tata Chemicals   [TATACHEM.NS]
  4. Tata Steel   [TATLY]

Enter number: 2

🚀 Starting AI Stock Analysis for: TCS.NS
...
📈 30-DAY FORECAST: BULLISH
🎯 Predicted Price Range: ₹3,800 - ₹4,100
📊 Confidence Level: 74%
💡 Key Reason: Strong Q3 earnings + positive institutional sentiment
✅ VERDICT: BUY
```

---

## ✨ Key Features

- 🌍 **Global Stock Search** — Covers NYSE, NASDAQ, NSE, BSE and more
- 🏢 **Smart Company Resolver** — Handles subsidiaries (Tata Motors vs TCS vs Tata Steel)
- 📈 **Real-Time Stock Data** — Live prices, PE ratio, market cap via Yahoo Finance
- 📰 **News Analysis** — Latest market-moving news from the last 30 days
- 💬 **Sentiment Analysis** — Reddit & social media investor mood
- 🎯 **30-Day Price Prediction** — Data-driven forecast with confidence score
- 📊 **Professional Report** — Saved as `stock_report.md`

---

## 🧠 Multi-Agent Architecture

```
User Input: "Tata Steel"
       ↓
Smart Company Resolver (Yahoo Finance search)
       ↓
┌─────────────────────────────────────────────┐
│             4 AI Agents Working             │
├─────────────────────────────────────────────┤
│ 📈 Stock Data Agent  → prices, PE, targets  │
│ 📰 News Agent        → latest news impact   │
│ 💬 Sentiment Agent   → Reddit investor mood │
│ 📊 Report Agent      → final report + BUY/HOLD/SELL │
└─────────────────────────────────────────────┘
       ↓
  stock_report.md  ✅
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core language |
| [CrewAI](https://crewai.com) | Multi-agent orchestration framework |
| Google Gemini / Together AI | Large Language Model |
| [Serper API](https://serper.dev) | Real-time web search for agents |
| [Yahoo Finance API](https://finance.yahoo.com) | Live stock data & global company search |
| python-dotenv | Secure API key management |

---

## 📁 Project Structure

```
stock-intelligence-agent/
│
├── main.py          ← Entry point + smart company resolver
├── agents.py        ← 4 AI agent definitions
├── tasks.py         ← Task assignments for each agent
├── tools.py         ← Web search tool setup
├── .env             ← API keys (not committed)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/stock-intelligence-agent.git
cd stock-intelligence-agent
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install crewai crewai-tools litellm yfinance requests python-dotenv
pip install "crewai[google-genai]"
```

### 4. Set up API keys

Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_gemini_key_here
SERPER_API_KEY=your_serper_key_here
```

| Key | Where to get it | Cost |
|---|---|---|
| Gemini API | [aistudio.google.com](https://aistudio.google.com/apikey) | Free |
| Serper API | [serper.dev](https://serper.dev) | Free (2500 searches) |

### 5. Run it
```bash
python main.py
```

---

## 📊 Sample Report Output

```
=== TATA CONSULTANCY SERVICES (TCS.NS) ===

1. COMPANY SNAPSHOT
   Leading IT services company, ₹14L Cr market cap, operates in 50+ countries.

2. KEY METRICS
   • Current Price: ₹3,912
   • 52-Week High/Low: ₹4,592 / ₹3,317
   • PE Ratio: 28.4
   • Analyst Target: ₹4,200

3. NEWS IMPACT
   • Strong Q3 FY25 results — revenue up 5.6% YoY ↑
   • New AI deal with European banking client ↑
   • Slight headcount reduction amid automation push ↓

4. SENTIMENT: BULLISH 📈
   Retail investors on Reddit optimistic about AI integration strategy.

5. 30-DAY PREDICTION
   📈 FORECAST: BULLISH
   🎯 Price Range: ₹3,950 - ₹4,200
   📊 Confidence: 71%
   💡 Reason: Post-earnings recovery + strong order book

6. VERDICT: BUY ✅
```

---

## 🌍 Supported Exchanges

NYSE · NASDAQ · NSE · BSE · LSE · TSE · FRA · and more via Yahoo Finance

---

## 📌 Notes

- Free API tiers have regional/rate limitations — a paid API key is recommended for production use
- Stock predictions are based on technical indicators, news sentiment, and analyst targets — **not financial advice**
- This project is for educational and portfolio purposes

---

## 👩‍💻 Author

**Shravani R S**  
M.Tech, IIIT Dharwad | AI/ML Engineer  
[LinkedIn](https://linkedin.com) · [GitHub](https://github.com)

---

⭐ Star this repo if you found it useful!