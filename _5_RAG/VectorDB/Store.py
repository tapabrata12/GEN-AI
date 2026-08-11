from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os
load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

nvidia_embeddings = NVIDIAEmbeddings(
  model="nvidia/nv-embedqa-e5-v5", 
  api_key=NVIDIA_API_KEY, 
  truncate="NONE", 
  )

loader = PyPDFLoader("_5_RAG/VectorDB/data/PolicyPaperServicesSector.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size= 1000, chunk_overlap= 100)

chunks = splitter.split_documents(docs)


vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=nvidia_embeddings,
    persist_directory="_5_RAG/database",  # Where to save data locally, remove if not necessary
)

vector_store.add_documents(chunks)
