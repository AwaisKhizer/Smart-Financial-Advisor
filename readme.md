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
├── agent.py             # AI-based financial functions |
├── app.py               # Main Streamlit application   |
├── supabaseclient.py    # Initializes Supabase client  |
├── utils.py             # Transaction functions (add/retrieve) |
├── .env                 # Environment variables (ignored in Git) |
├── .gitignore                                          |
├── README.md            # Project documentation        |
 
## 🤖 AI Integration (LangChain + Groq)

The app uses **LangChain** to handle LLM interactions.  
Specifically, it uses:

```python
from langchain_groq import ChatGroq

###  📄 File Descriptions

- **`agent.py`**  
  Defines 3 core AI-powered functions:  
  - `run_budget_analysis()`: AI feedback on income vs expenses  
  - `run_savings_advice()`: AI savings suggestions  
  - `run_goal_planning()`: Create a 6-month savings plan

- **`app.py`**  
  Main Streamlit UI with navigation, forms, and transactions display.

- **`supabaseclient.py`**  
  Initializes Supabase connection using `.env` variables.

- **`utils.py`**  
  Handles data storage/retrieval from Supabase.

---

## 🧰 Setup Instructions

### 🔐 Prerequisites
- Python 3.8+
- Supabase account
- Text editor (VS Code recommended)
- Terminal/Command Prompt

---

### 🧾 Steps

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/smart-financial-advisor.git
cd smart-financial-advisor
