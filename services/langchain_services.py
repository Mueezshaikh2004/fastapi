import os

from dotenv import load_dotenv

load_dotenv()

try:
    from langchain_community.chat_message_histories import ChatMessageHistory
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.runnables.history import RunnableWithMessageHistory
    from langchain_groq import ChatGroq
except ModuleNotFoundError:
    ChatMessageHistory = None
    ChatPromptTemplate = None
    MessagesPlaceholder = None
    RunnableWithMessageHistory = None
    ChatGroq = None

llm = None
prompt_with_memory = None
chain_with_memory = None
store = {}

if ChatGroq is not None and ChatPromptTemplate is not None and MessagesPlaceholder is not None:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.5,
    )
    prompt_with_memory = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )
    chain_with_memory = prompt_with_memory | llm


def get_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory() if ChatMessageHistory is not None else []
    return store[session_id]


def ask_career_chatbot_response(question: str, session_id: str) -> str:
    if chain_with_memory is None or RunnableWithMessageHistory is None:
        return "Career chatbot service is unavailable because the required LangChain packages are not installed."

    chat_with_memory = RunnableWithMessageHistory(
        runnable=chain_with_memory,
        get_session_history=get_history,
        input_messages_key="user_query",
        history_messages_key="history",
    )
    response = chat_with_memory.invoke(
        {"user_query": question},
        config={"configurable": {"session_id": session_id}},
    )
    return response.content if hasattr(response, "content") else str(response)

