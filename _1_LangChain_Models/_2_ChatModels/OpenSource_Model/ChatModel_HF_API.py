from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

print("Token loaded:", os.getenv("HUGGINGFACE_API_TOKEN") is not None)

llm = HuggingFaceEndpoint(
	model = "meta-llama/Llama-3.1-8B-Instruct",
	task = "text-generation",
	temperature=0.7,
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Do you know about 'Your Name' anime?")

print(result.content)