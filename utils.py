from supabase_client import supabase 
from datetime import datetime

def add_transaction(t_type, category, amount, description):
    now = datetime.now()
    month_str = now.strftime("%Y-%m")
    
    supabase.table("transactions").insert({
        "type": t_type,
        "category": category,
        "amount": amount,
        "description": description,
        "month": month_str,
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S")
    }).execute()

def get_transactions(month=None):
    query = supabase.table("transactions").select("*").order("timestamp", desc=True)
    if month:
        query = query.eq("month", month)
    data = query.execute()
    return data.data if data.data else []

def delete_transaction(transaction_id):
    supabase.table("transactions").delete().eq("id", transaction_id).execute()
