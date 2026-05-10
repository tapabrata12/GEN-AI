from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

loader = TextLoader('_5_RAG/text_splitter/AI.txt')
docs = loader.load()

docs = docs[0].page_content

text_spliter = CharacterTextSplitter(
    separator='',
    chunk_size=200,
    chunk_overlap=1,
)

chunks = text_spliter.split_text(text=docs) # type: ignore

for i in chunks:
    print(i)
    print('--------------------------------------------------------')