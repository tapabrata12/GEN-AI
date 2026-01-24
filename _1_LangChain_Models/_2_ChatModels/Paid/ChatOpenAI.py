from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("OPENAI_API_KEY")
print(key)


ChatMODEL = ChatOpenAI(model="gpt-3.5-turbo",temperature=.5)
reply = ChatMODEL.invoke("What is your name Anime ?")
print(reply.containt)
"""
!!! This code will not execute because to generate reposes we need minimum 5$ recharge which I don't have.
"""