from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import os

load_dotenv()

# Nemotron 3 Ultra - frontier reasoning and agentic workflows
llm = ChatNVIDIA(model="nvidia/nemotron-3-ultra-550b-a55b", api_key=os.getenv("NVIDIA_API_KEY"))
result = llm.invoke("Capital of India?")
print(result.content)

from langchain_nvidia_ai_endpoints import ChatNVIDIADynamo

llm2 = ChatNVIDIADynamo(
    base_url="http://localhost:8099/v1",
    model="nvidia/nemotron-3-ultra-550b-a55b",
    osl=512,             # expected output sequence length (tokens)
    iat=250,             # expected inter-arrival time (ms)
    latency_sensitivity=1.0,
    priority=1,
)
result = llm2.invoke("Summarize KV cache routing in one sentence.")
print(result.content)