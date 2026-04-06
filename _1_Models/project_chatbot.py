from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

model = ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct', temperature=0.7, max_tokens=500)
memory = []
while True:
    if input("Do you want to exit? (yes/no): ").lower() == 'yes':
        break
    user_input = input("You: ")
    memory.append(("user", user_input)) #type:ignore
    response = model.invoke(memory) #type:ignore
    memory.append(("assistant", response.content)) #type:ignore
    print(f'Chatbot: {response.content}', end='\n\n') #type:ignore

print(memory) #type:ignore