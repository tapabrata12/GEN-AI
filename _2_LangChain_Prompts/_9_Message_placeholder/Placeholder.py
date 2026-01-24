from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support assistant agent'),
    MessagesPlaceholder(variable_name='chat_hist'),
    ('human', '{query}')
])

chat_hist = []

# load chat history
with open('History.txt') as f:
    chat_hist.extend(f.readlines())

prompt = chat_template.invoke({'chat_hist': chat_hist, 'query': "Where is my refund ?"})

print(prompt)
