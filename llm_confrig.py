from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()

goq_api = os.getenv('GROQ_API_KEY')
gemini_api = os.getenv('GEMINI_API_KEY')

# llm = LLM(
#     model="gemini/gemini-1.5-pro-002",
#     api_key= gemini_api
# )


llm = LLM(
    model="groq/llama3-8b-8192",
    api_key=goq_api
)