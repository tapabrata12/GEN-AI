from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

if load_dotenv():
    print("Environment variables loaded successfully")
else:
    print("Environment variables not loaded")

model = ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

responses = model.batch([
    "What is the Capital of India",
    "What is the Capital of USA",
    "What is the Capital of UK",
    "What is the Capital of France",
    "What is the Capital of Germany",
    "What is the Capital of China",
], config={
    'max_concurrency': 5,  # Limit to 5 parallel calls
})

for response in responses:
    print(response.content)