from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=2,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

responce = model.invoke("What is the capital of India?")

print(responce.content)