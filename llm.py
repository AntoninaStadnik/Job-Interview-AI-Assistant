from langchain_google_genai import ChatGoogleGenerativeAI
from config import api_key


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=api_key
)