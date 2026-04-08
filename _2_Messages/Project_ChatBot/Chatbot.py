from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, BaseMessage

model = ChatGroq(model='openai/gpt-oss-120b', temperature=0.7, max_tokens=500)
memory: list[BaseMessage] = []  # ← explicit type, Pylance now knows what's inside

SYSTEM_PROMPTS = {
    1: "You are a helpful AI assistant. Answer the user's questions as best as you can.",
    2: "You are an angry AI assistant. Draft and give answers according to your personality.",
    3: "You are a sad AI assistant. Draft and give answers according to your personality.",
}

def set_mode(mode: int):
    memory.clear()
    if mode in SYSTEM_PROMPTS:
        memory.append(SystemMessage(content=SYSTEM_PROMPTS[mode]))

def get_response(prompt: str) -> str:
    memory.append(HumanMessage(content=prompt))
    response = model.invoke(memory)
    memory.append(AIMessage(content=response.content))  # type: ignore
    return str(response.content)  # type: ignore