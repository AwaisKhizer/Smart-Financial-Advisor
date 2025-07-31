from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(temperature=0.3, model="llama3-70b-8192", groq_api_key=os.getenv("GROQ_API_KEY"))
