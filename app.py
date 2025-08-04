import streamlit as st
from datetime import datetime
from utils import add_transaction, get_transactions, delete_transaction
from agents import run_budget_analysis, run_savings_advice, run_goal_planning

st.set_page_config(page_title="Smart Financial Advisor", layout="wide")
st.sidebar.title("\U0001F4DA Navigation")

option = st.sidebar.radio("Go to", [
    "\U0001F4C8 Expense Tracker",
    "\U0001F4C8 Budget Analysis",
    "\U0001F4A1 Savings Advisor",
    "\U0001F3AF Goal Planner"
])

st.title("\U0001F916 Smart Financial Advisor")

if option == "\U0001F4C8 Expense Tracker":
    st.header("\U0001F4B0 Monthly Financial Input")

    selected_month = st.selectbox("Select Month", ["Current Month", "Custom"])
    if selected_month == "Custom":
        month_input = st.text_input("Enter month (YYYY-MM)", value=datetime.now().strftime("%Y-%m"))
    else:
        month_input = datetime.now().strftime("%Y-%m")

    st.subheader("➕ Add Income")
    with st.form("income_form"):
        income_category = st.selectbox("Income Category", ["Salary", "Freelance", "Other"])
        income_amount = st.number_input("Amount (PKR)", min_value=0.0, key="inc_amt")
        income_description = st.text_input("Income Description")
        income_submit = st.form_submit_button("Add Income")
        if income_submit:
            add_transaction("income", income_category, income_amount, income_description)
            st.success("Income added!")

    st.subheader("➖ Add Expense")
    with st.form("expense_form"):
        expense_category = st.selectbox("Expense Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
        expense_amount = st.number_input("Amount (PKR)", min_value=0.0, key="exp_amt")
        expense_description = st.text_input("Expense Description")
        expense_submit = st.form_submit_button("Add Expense")
        if expense_submit:
            add_transaction("expense", expense_category, expense_amount, expense_description)
            st.success("Expense added!")

    st.header("\U0001F4CB Transactions")
    transactions = get_transactions(month_input)
    if not transactions:
        st.info("No transactions found.")
    else:
        for t in transactions:
            label = "🟢 Income" if t["type"] == "income" else "🔴 Expense"
            with st.expander(f"{label} - {t['category']} - Rs. {t['amount']}"):
                st.write(f"\U0001F4DD {t['description']}")
                st.write(f"\U0001F552 {t['timestamp']}")
                
                if st.button("🗑️ Delete", key=f"del_{t['id']}"):
                    delete_transaction(t["id"])
                    st.success("Transaction deleted!")
                    st.rerun()

elif option == "\U0001F4C8 Budget Analysis":
    st.header("\U0001F4C8 Budget Analysis with AI")
    result = run_budget_analysis()
    st.write(result)

elif option == "\U0001F4A1 Savings Advisor":
    st.header("\U0001F4A1 Savings Suggestions from AI")
    result = run_savings_advice()
    st.write(result)

elif option == "\U0001F3AF Goal Planner":
    st.header("\U0001F3AF Goal-Based Saving Plan")
    result = run_goal_planning()
    st.write(result)
