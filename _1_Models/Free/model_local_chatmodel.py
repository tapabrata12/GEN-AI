import os
from pathlib import Path

BASE_DIR = Path.cwd() / "my_models"
BASE_DIR.mkdir(parents=True, exist_ok=True)  

os.environ["HF_HOME"] = str(BASE_DIR)
os.environ["HF_HUB_CACHE"] = str(BASE_DIR / "hub")
os.environ["TRANSFORMERS_CACHE"] = str(BASE_DIR / "transformers")

print(f"Models will download to: {os.environ['HF_HOME']}")

from dotenv import load_dotenv
load_dotenv(override=False)  

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    model_provider='huggingface',
    temperature=0.7,
    max_tokens=1024
)

response = model.invoke('What is the Capital of India?')
print(response.content)  # type: ignore