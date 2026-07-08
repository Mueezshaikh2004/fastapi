import os

from dotenv import load_dotenv

load_dotenv()

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ModuleNotFoundError:
    ChatGoogleGenerativeAI = None

model = None
if ChatGoogleGenerativeAI is not None:
    model = ChatGoogleGenerativeAI(
        api_key=os.getenv("GEMINIAPIKEY"),
        model="gemini-2.5-flash",
        temperature=0.5,
    )


def llm_response(question: str):
    if model is None:
        return "LLM service is unavailable because the required package is not installed."

    response = model.invoke(question)
    return response.content