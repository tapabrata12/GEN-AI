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
os.environ['HF_HOME'] = r"D:\GEN-AI\LLM_Downloads"

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
"""
Example: [[ 5.31072460e-01  1.25747872e-01 -3.03747913e-04 -6.00734540e-02]]
But we need 1D list that's why we store the 0th row of that 2D list by '[0]'

So we get: [5.31072460e-01  1.25747872e-01 -3.03747913e-04 -6.00734540e-02] insted of [[ 5.31072460e-01  1.25747872e-01 -3.03747913e-04 -6.00734540e-02]]
"""
similarity_score = cosine_similarity([vector_query],vectors)[0]

# ---------------------------------------------------------
# Step 1: give indices to all similarity scores
# Step 2: convert it to a list
# Step 3: do sorting based on similarity score
# Step 4: take out the last element as it has the biggest chance to relate with given question
# ---------------------------------------------------------

# index,score = sorted(list(enumerate(similarity_score)),key=lambda x:x[1])[-1]

# print(sentences[index])
# print("Similarity: ",score*100,"%")


"""
If you are unable to understand the above code then you can use the below code it way easier 
to understand
# ----------------------------------------------------------------------------------------------------------------------------------
    -> Basically we got and N-Dimensional array into the `similarity_score` and our moto is to
        -> Convert it into a 1D list
        -> Find the maximum value in the `similarity_score` and its index
        -> Extract those values into 2 consicutive variables `MAX_VALUE` and `INDEX`
        -> Print the `sentences` based on the `INDEX` bacause order of the provided answere list and `similarity_score`
        is same so if we get the index of the maximum value in `similarity_score` then we can get the answer from the `sentences` list
        at that same index
# ----------------------------------------------------------------------------------------------------------------------------------
"""
similarity_score = list(similarity_score)
MAX_VALUE = similarity_score[0]
INDEX = 0
for i in range(len(similarity_score)):

    if similarity_score[i] > MAX_VALUE:
        MAX_VALUE = similarity_score[i]
        INDEX = i

print(sentences[INDEX])
print("Similarity: ",MAX_VALUE*100,"%")