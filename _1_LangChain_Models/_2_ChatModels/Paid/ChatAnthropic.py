from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

ChatMODEL = ChatAnthropic(model_name='claude-opus-4-20250514',timeout=None,stop=['Bad words'])

result = ChatMODEL.invoke("What is AI ?")

print(result.containt)
"""
!!! This code will not execute because to generate reposes we need minimum 5$ recharge which I don't have.
"""