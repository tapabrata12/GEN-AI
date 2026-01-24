from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

if load_dotenv():
    print("Environment variables loaded successfully")
else:
    print("Environment variables not loaded")

model = ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

respoce = model.stream("Write a 1000 paragraph on AI")

for chunk in respoce:
    print(chunk.text, end="", flush=True)