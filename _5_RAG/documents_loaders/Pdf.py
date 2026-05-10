from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

loader = PyPDFLoader('_5_RAG/documents_loaders/AI.pdf')

docs = loader.load()

prompt = ChatPromptTemplate.from_messages([  # type: ignore
    ('system', 'You are a helpful assistant summerizing the content of a PDF document.'),
    ('human', '{pdf_content}')
])

response = ''

for doc in docs:
    pdf_content = doc.page_content
    response = response + pdf_content

final_prompt = prompt.format(pdf_content=response)

model = ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct', temperature=0.7)

answere = model.invoke(final_prompt)
print(answere.content) # type: ignore