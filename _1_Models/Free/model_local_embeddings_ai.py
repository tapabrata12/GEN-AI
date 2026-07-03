from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os
from pathlib import Path
BASE_DIR = Path.cwd() / "my_models"
BASE_DIR.mkdir(parents=True, exist_ok=True)  

os.environ["HF_HOME"] = str(BASE_DIR)
os.environ["HF_HUB_CACHE"] = str(BASE_DIR / "hub")
os.environ["TRANSFORMERS_CACHE"] = str(BASE_DIR / "transformers")

print(f"Models will download to: {os.environ['HF_HOME']}")


# Nemotron 3 Ultra - frontier reasoning and agentic workflows
llm = ChatNVIDIA(model="nvidia/nemotron-3-ultra-550b-a55b")
result = llm.invoke("Plan a three-step research workflow for competitive analysis.")
print(result.content)