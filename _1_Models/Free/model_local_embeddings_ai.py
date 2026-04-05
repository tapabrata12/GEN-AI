import os
from pathlib import Path
BASE_DIR = Path.cwd() / "my_models"
BASE_DIR.mkdir(parents=True, exist_ok=True)  

os.environ["HF_HOME"] = str(BASE_DIR)
os.environ["HF_HUB_CACHE"] = str(BASE_DIR / "hub")
os.environ["TRANSFORMERS_CACHE"] = str(BASE_DIR / "transformers")

print(f"Models will download to: {os.environ['HF_HOME']}")

from langchain_huggingface.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

texts = ["Hello", "H1", "Tapabrata Chowdhury"]

vector = embeddings.embed_documents(texts)

print(vector)