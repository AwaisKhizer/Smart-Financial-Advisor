from llm import llm
from utils import get_transactions
from datetime import datetime

def run_budget_analysis():
    month = datetime.now().strftime("%Y-%m")
    transactions = get_transactions(month)
    if not transactions:
        return "No data found for budget analysis."

    income = [t for t in transactions if t["type"] == "income"]
    expenses = [t for t in transactions if t["type"] == "expense"]

    prompt = "Here's my monthly financial data:\n\nIncome:\n"
    for i in income:
        prompt += f"- {i['category']}: Rs. {i['amount']} ({i['description']})\n"

    prompt += "\nExpenses:\n"
    for e in expenses:
        prompt += f"- {e['category']}: Rs. {e['amount']} ({e['description']})\n"

    prompt += "\nPlease analyze my budget: total income vs total expenses, identify overspending, and give 3 budget tips."

    return llm.invoke(prompt).content

def run_savings_advice():
    month = datetime.now().strftime("%Y-%m")
    transactions = get_transactions(month)
    if not transactions:
        return "No expenses available to analyze for savings."

    expenses = [t for t in transactions if t["type"] == "expense"]

    prompt = "Here are my expenses this month:\n"
    for exp in expenses:
        prompt += f"- {exp['category']}: Rs. {exp['amount']}\n"

    prompt += "\nSuggest 3 specific ways I can save more money next month."

    return llm.invoke(prompt).content

def run_goal_planning():
    prompt = (
        "I want to save Rs. 100,000 in 6 months. Give me a monthly goal plan "
        "considering lifestyle expenses like food, bills, transport, and shopping."
    )
    return llm.invoke(prompt).content
