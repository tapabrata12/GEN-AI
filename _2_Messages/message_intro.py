from dotenv import load_dotenv
from langchain.messages import HumanMessage, SystemMessage,AIMessage
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-120b',temperature=1)

messages = [SystemMessage(content="You are very helpful AI assistent guide the user for his given query")]

print("Welcome to the AI assistant! Type 'exit' to quit.")

while True:
    user_input= input("User: ")

    if user_input.lower() == 'exit':
        break

    messages.append(HumanMessage(content=user_input)) # type: ignore
    response = llm.invoke(messages)
    print(f"AI: {response.content}") # type: ignore
    messages.append(AIMessage(content=response.content)) # type: ignore

print("Goodbye!")
