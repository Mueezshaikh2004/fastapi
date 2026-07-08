import os
from dotenv import load_dotenv
try:
    from langchain_groq import ChatGroq
    from langchain_core.prompts import ChatPromptTemplate
except ModuleNotFoundError:
    ChatGroq = None
    ChatPromptTemplate = None

load_dotenv()

llm = None
resume_prompt = None
resume_chain = None

if ChatGroq is not None and ChatPromptTemplate is not None:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3,
    )

    resume_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a professional resume analyser.
Analyse the given resume text and provide:
1. Key Skills found
2. Experience Level (Junior/Mid/Senior)
3. Strengths
4. Areas to Improve
5. Suggested Job Roles

Keep the analysis short and structured."""),
        ("human", "{resume_text}")
    ])

if resume_prompt is not None and llm is not None:
    resume_chain = resume_prompt | llm


def analyse_resume(resume_text: str) -> str:
    if resume_chain is None:
        return "Resume analysis service is unavailable because the required LangChain packages are not installed."

    response = resume_chain.invoke({"resume_text": resume_text})
    return response.content if hasattr(response, "content") else str(response)