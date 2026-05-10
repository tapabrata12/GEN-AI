from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader

loader = TextLoader('_5_RAG/documents_loaders/AI.txt')
documents = loader.load()

prompt = ChatPromptTemplate.from_messages([ # type: ignore
    ('system', 'You are a text summarizer. Summarize the following text with 25% of the original word count'),
    ('human', '{text}')
])

final_prompt = prompt.invoke({ # type: ignore
    'text': documents[0].page_content
})

llm = ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct', temperature=0.7)

result = llm.invoke(final_prompt)

print(result.content) # type: ignore