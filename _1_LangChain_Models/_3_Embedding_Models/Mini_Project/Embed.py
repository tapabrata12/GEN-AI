# ---------------------------------------------------------
# This is a project about where we generate embeddings of both
# question and answer. Then based on the given question program
# deduce which answer to pick. Here It try to find the similarity
# using vector embeddings.
# ---------------------------------------------------------

from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import os
# ---------------------------------------------------------
# Fix Hugging Face Xet issue: force fallback to HTTP
# ---------------------------------------------------------
os.environ["HF_HUB_ENABLE_XET"] = "0"
# Optional: set custom model cache directory
os.environ['HF_HOME'] = r"D:\Python_Stack\Langchain\LLM_Downloads"

embeddings = HuggingFaceEmbeddings(model ="sentence-transformers/all-mpnet-base-v2")

sentences = [
    "Artificial Intelligence is transforming industries by automating complex tasks.",
    "The Amazon rainforest produces nearly 20% of the world's oxygen supply.",
    "Good financial habits, like budgeting and saving, can reduce long-term stress.",
    "Exercise not only strengthens the body but also improves mental health."
]

vectors = embeddings.embed_documents(sentences)

query = input("Enter the question but must be related any of that four questions: ")

vector_query = embeddings.embed_query(query)

# Calculating the similarity score of given query to the pre-generated answers
# Actually it usually give 2D List, but we need 1D that's why we store the 0th row of that 2D list by '[0]'
similarity_score = cosine_similarity([vector_query],vectors)[0]

# ---------------------------------------------------------
# Step 1: give indices to all similarity scores
# Step 2: convert it to a list
# Step 3: do sorting based on similarity score
# Step 4: take out the last element as it has the biggest chance to relate with given question
# ---------------------------------------------------------

index,score = sorted(list(enumerate(similarity_score)),key=lambda x:x[1])[-1]

print(sentences[index])
print("Similarity: ",score*100,"%")