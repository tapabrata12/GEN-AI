from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

loader = WebBaseLoader('https://en.wikipedia.org/wiki/Artificial_intelligence')

data = loader.load()

prompt = ChatPromptTemplate.from_messages([ # type: ignore
    ('system', 'You are a text summarizer. Summarize the following text with 25% of the original word count'),
    ('human', '{text}')
])

final_prompt = prompt.format(text = data[0].page_content.strip())

llm = ChatGroq(model='openai/gpt-oss-120b', temperature=0.7)

result = llm.invoke(final_prompt)

print(result.content) # type: ignore