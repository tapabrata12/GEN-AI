from langchain_openai import OpenAI
from dotenv import load_dotenv

# Loading Model API keys from .env file
load_dotenv()

# Creating model instance and selecting the name of the model
llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India ?")

print(result)

"""
!!! This code will not execute because to generate reposes we need minimum 5$ recharge which I don't have.
"""