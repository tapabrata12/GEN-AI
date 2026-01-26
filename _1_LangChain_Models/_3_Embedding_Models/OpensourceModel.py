from langchain_huggingface import HuggingFaceEmbeddings
import os

# ---------------------------------------------------------
# Fix Hugging Face Xet issue: force fallback to HTTP
# ---------------------------------------------------------
os.environ["HF_HUB_ENABLE_XET"] = "0"
# Optional: set custom model cache directory
os.environ['HF_HOME'] = r"D:\GEN-AI\LLM_Downloads"


embeddings = HuggingFaceEmbeddings(model ="sentence-transformers/all-mpnet-base-v2")

text = "I am a good boy"
vector = embeddings.embed_query(text)
print(str(vector))

print("Now the below is list of documents: ")
texts = [
	"Kolkata is the capital of West bengal",
	"Delhi is the capital of India",
	"I am a good boy",
]

vectors = embeddings.embed_documents(texts)

print(str(vectors))
