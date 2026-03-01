# 🤖 AI Stock Intelligence System

A multi-agent AI system that performs end-to-end stock analysis for any company worldwide using **CrewAI** framework.

---

## 🌟 Features

- 🔍 **Smart Company Search** — Type "Tata" or "Jio" and get all matching companies across NSE, BSE, NYSE, NASDAQ
- 📊 **Real-time Stock Data** — Current price, market cap, PE ratio, 52-week high/low
- 📰 **News Analysis** — Latest news and its impact on stock performance  
- 💬 **Sentiment Analysis** — Market sentiment from news and social media
- 📈 **30-Day Price Prediction** — Forecast with confidence score and BUY/HOLD/SELL verdict
- 🌍 **Global Coverage** — Works for any stock worldwide

---

## 🏗️ Architecture

The system uses **4 specialized AI agents** working in sequence:

| Agent | Role |
|-------|------|
| 📊 Stock Data Specialist | Fetches real-time price, market cap, PE ratio, analyst targets |
| 📰 News Analyst | Finds and analyzes latest news about the company |
| 💬 Sentiment Analyst | Analyzes market sentiment and investor mood |
| 📝 Report Generator | Combines all data into a professional investment report |

---

## 🛠️ Tech Stack

- **CrewAI** — Multi-agent orchestration framework
- **Google Gemini / LLM** — Language model for agent intelligence
- **Serper API** — Real-time web search for news and data
- **Yahoo Finance API** — Global company search and stock data
- **Python** — Core language

---

## 📁 Project Structure

```
stock-intelligence-agent/
├── main.py          # Entry point, company search, crew orchestration
├── agents.py        # 4 AI agent definitions
├── tasks.py         # Task definitions for each agent
├── tools.py         # Search tools and Yahoo Finance integration
├── .env             # API keys (not committed)
└── requirements.txt # Dependencies
```

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/stock-intelligence-agent.git
cd stock-intelligence-agent
```

### 2. Install dependencies
```bash
pip install crewai crewai-tools python-dotenv yfinance requests
```

### 3. Set up API keys
Create a `.env` file:
```
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

Get your free API keys:
- Gemini: [aistudio.google.com](https://aistudio.google.com)
- Serper: [serper.dev](https://serper.dev)

### 4. Run the system
```bash
python main.py
```

---

## 💡 Usage Example

```
🔎 Enter company name or ticker: tata

🔍 Found multiple companies matching 'tata':
  1. Tata Communications Limited  | TATACOMM.NS | NSE
  2. Tata Consultancy Services    | TCS.NS       | NSE
  3. Tata Chemicals Limited       | TATACHEM.NS  | NSE
  4. Tata Steel Limited           | TATLY        | NYSE

Enter number: 2

✅ Selected: Tata Consultancy Services [TCS.NS]
🚀 Starting AI Stock Analysis...
```

**Sample Output:**
```
📊 STOCK REPORT: TCS.NS
Current Price: ₹3,456
Market Cap: ₹12.5L Cr
PE Ratio: 28.4

📈 FORECAST: BULLISH
🎯 Predicted Price Range: ₹3,600 - ₹3,800
📊 Confidence Level: 72%
💡 Key Reason: Strong Q3 results + positive IT sector outlook
✅ VERDICT: BUY
```

---

## ⚠️ Note

This project requires a valid LLM API key to run. Free tier options include Google Gemini API (regional availability may vary) or Together AI. The system architecture and code are fully functional — API availability depends on your region and account status.

---

## 👩‍💻 Author

**Shravani R S**  
M.Tech AI/ML — IIIT Dharwad  
[LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/YourUsername)

---

## 📄 License

MIT License — feel free to use and modify!