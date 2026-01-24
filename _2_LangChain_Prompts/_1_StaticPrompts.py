from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

print("Token loaded:", os.getenv("HUGGINGFACEHUB_API_TOKEN") is not None)

llm =  HuggingFaceEndpoint(
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B",
    task="text-generation",
    temperature=0.7
)
model = ChatHuggingFace(llm=llm)

# ---------------------------------------------------------
# This is the example of static prompt where we manually
# input the prompt to generate required answer
# ---------------------------------------------------------

result = model.invoke("Hello give me the name of the capital of India")


print(result.content)