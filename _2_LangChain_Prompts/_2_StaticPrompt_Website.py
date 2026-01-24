from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
	model="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B",
	task="text-generation",
	temperature=0.7
)

model = ChatHuggingFace(llm=llm)

# ---------------------------------------------------------
# Although we can send our prompts through website but still it is
# an example of Static prompt not dynamic prompt. As in the previous file
# we write our prompt while writing our code and here we write that in website.
# In the Next File I will Show you what dynamic really is
# ---------------------------------------------------------
# Summarizer
st.title("Summarizer AI")
prompt = st.text_input("Enter the your topic name: ")
button = st.button("Summarize")

if button:
	result = model.invoke(prompt)
	st.write(result.content)
	st.success("Summarization successfully completed")
