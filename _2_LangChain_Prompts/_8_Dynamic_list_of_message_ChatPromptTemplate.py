from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
	('system',"You are very helpful {domain} expert"),
	('human',"Explain in simple terms about {topic}")
	
])

prompt = chat_template.invoke({'domain': 'Cricket','topic':'Cricket'})

print(prompt)