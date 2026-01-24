from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv


class Summerize:
	def __init__(self, text: str):
		
		self.prompt = text
		

	def generate_paragraph(self):
		
		load_dotenv()
		llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation", temperature=0.7)
		model = ChatHuggingFace(llm=llm)
		result = model.invoke(self.prompt)
		return result.content
		