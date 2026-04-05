from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)
text = "This is a test document"
text_array = ["This is a test document", "This is another test document", "I am a boy"]
query_result = embeddings.embed_query(text)
query_result_array = embeddings.embed_documents(text_array)

print(query_result)
print("-------------------------------------------------------------------------------------------------------------------------")
print(query_result_array)