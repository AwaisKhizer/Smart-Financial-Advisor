# 🤖 Smart Financial Advisor

A web-based personal finance management application built with **Streamlit**, **Supabase**, and **AI-powered financial analysis** via **LangChain + Groq**.

The **Smart Financial Advisor** helps users:
- Track their income and expenses
- Analyze their budget
- Receive personalized savings advice
- Plan for long-term financial goals

---



## ✅ Features

### 📊 Expense Tracker
- Add **income** and **expense** transactions with category, amount, and description
- View a detailed transaction list for the current or custom month
- Visual indicators: 🟢 for income, 🔴 for expenses (expandable details)

### 📈 Budget Analysis
- AI-driven summary of **monthly income vs expenses**
- Highlights **overspending patterns**
- Provides **three actionable budget tips**

### 💡 Savings Advisor
- Analyzes monthly expenses
- Suggests **3 specific ways to save more**
- Personalized based on user spending habits

### 🎯 Goal Planner
- Generates a **monthly savings plan** to reach a target goal (e.g., Rs. 100,000 in 6 months)
- Considers essential expenses like **food, bills, transport, shopping**

---

## 🛠 Tech Stack

| Layer            | Technology                                   |
|------------------|-----------------------------------------------|
| Frontend         | Streamlit (Python Web UI)                     |
| Backend          | Supabase (PostgreSQL BaaS)                    |
| AI Integration   | LangChain + Groq (LLaMA via `langchain_groq`) |
| Configuration    | python-dotenv for environment variables       |
| Core Libraries   | `datetime`, `os`                              |

---
## 📁 Project Structure
smart-financial-advisor/
├── agent.py # AI-based financial functions
├── app.py # Main Streamlit application
├── supabaseclient.py # Initializes Supabase client
├── utils.py # Transaction functions (add/retrieve)
├── .env # Environment variables (ignored in Git)
├── .gitignore # Git ignore file
├── requirements.txt # Python dependencies
├── README.md # Project documentation

---
## 🧠 AI Agent Logic (LangChain + Groq)

The app uses Groq’s **LLaMA 3** model via **LangChain** to generate insights from your financial data:

### `run_budget_analysis()`
- Analyzes income vs expenses
- Identifies overspending
- Provides 3 smart budgeting tips

### `run_savings_advice()`
- Evaluates monthly expenses
- Suggests 3 personalized ways to reduce spending

### `run_goal_planning()`
- Plans how to save Rs. 100,000 in 6 months
- Distributes savings based on expense types

LLM is initialized via:

```python
from langchain_groq import ChatGroq
llm = ChatGroq(api_key=GROQ_API_KEY, model="llama3-8b-8192")
 
