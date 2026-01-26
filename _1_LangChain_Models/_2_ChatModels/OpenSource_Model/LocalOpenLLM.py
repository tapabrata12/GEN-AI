from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import torch.cuda as cuda
import os

# ---------------------------------------------------------
# Fix Hugging Face Xet issue: force fallback to HTTP
# ---------------------------------------------------------
os.environ["HF_HUB_ENABLE_XET"] = "0"

# Optional: set custom model cache directory
os.environ['HF_HOME'] = r"D:\GEN-AI\LLM_Downloads"

if cuda.is_available():
    device = 0 # Use first GPU
else:
    device = -1 # Use CPU

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    device=device,
    pipeline_kwargs= dict(
	max_new_tokens=100,   # control output length
    temperature=0.5,      # creativity
    )
)

# Wrap for LangChain Chat interface
chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("Capital of India?")
print("\n=== Model Response ===")
print(response.content)