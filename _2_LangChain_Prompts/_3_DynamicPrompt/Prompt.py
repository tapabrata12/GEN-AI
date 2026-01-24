# ------------------------------------------------------------------------------------------------------------------
#                                   Now this is the Real example of Dynamic prompt
# Here I primitively make a prompt what should be the nature and length for the given Query so that every user gets
# same nature of answer for every possible query in short At previous file we uncontrolledly passes query but this
# we pass query in control manner
# ------------------------------------------------------------------------------------------------------------------

# Importing Prompt Template
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
# Make class
class Summerize:
	def __init__(self,text:str,length:str):
		# 1. Take two inputs from user topic name and length
		self.prompt = text
		self.length = length
	
	
	@staticmethod
	def model_answer(prompt):
		
		# 6. Fetching HuggingFace API from .env file
		load_dotenv()
		# 7. Defining model and the parameter
		llm = HuggingFaceEndpoint(
			model="meta-llama/Llama-3.1-8B-Instruct",
			task="text-generation",
			temperature=0.7
		)
		
		# 7. Defining model and the parameter (Alternative choice)
		# llm = HuggingFaceEndpoint(
		# 	model="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B",
		# 	task="text-generation",
		# 	temperature=0.7
		# )
		
		# 8. Make the model instance with pre-defined name and parameter
		model = ChatHuggingFace(llm=llm)
		# 9. Giving the Prompt to the model and try to generate answer and save it to 'result' variable
		result = model.invoke(str(prompt))
		# 10. Return the content part of the result from where it has been called
		return result.content
		
	def generate_paragraph(self):
		# 2. Pass that to two length and topic the function
		text = self.prompt
		range_text = self.length
		
		# 3. Make my organised prompt with that two attributes (topic and length)
		prompt_obj = PromptTemplate(
			template="""
		    You are an assistant tasked with generating a focused explanation.

		    **Task:**
		    Explain about "{text}" in a coherent and informative way.

		    **Requirements:**
		    - Length: approximately {range_text}.
		    - Stay strictly on-topic and avoid irrelevant details.
		    - Use clear, simple, and professional language.
		    - Do not guess or hallucinate.
		      - If the required information is not available in the reference paper, respond with exactly:
		        "Insufficient information available"
		    - Ensure the explanation flows logically as a well-structured paragraph.
		    - Maintain factual accuracy and align with the requested style and length.

		    Now, generate the explanation.
		    """,
			input_variables=['text', 'range_text'],
			validate_template=True
		)
		
		# 4. Accepting the length and topic to fetch with the previously made prompt
		prompt = prompt_obj.invoke({
			'text': text,
			'range_text': range_text
		})
		
		# 5. Calling the model function and giving the prompt
		result = self.model_answer(prompt)
		
		# 11. Return the result to the UI.py file where it has been seen in frontend
		return result