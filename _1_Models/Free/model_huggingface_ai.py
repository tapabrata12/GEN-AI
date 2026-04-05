from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(model='deepseek-ai/DeepSeek-R1',task="text-generation",temperature=0.7,provider="auto")
model = ChatHuggingFace(llm=llm)
response = model.invoke("What is the capital of India?")
print(response.content) # type: ignore