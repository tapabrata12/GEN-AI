from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatMODEL = GoogleGenerativeAI(model='gemini-3-flash-preview')

result = chatMODEL.invoke("What is the capital of India ?")
print(result)

"""
!!! This code will not execute because to generate reposes we need minimum 5$ recharge which I don't have.
"""