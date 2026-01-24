import streamlit as st
from Prompt import Summerize
# Summarizer
st.title("Summarizer AI")
prompt = st.text_input("Enter the your topic name: ")
dropdown = st.selectbox("Choose the length:",['Small: 5 lines','Medium: 10 to 15 lines','Large: 20 to 30 lines'])
button = st.button("Summarize")

if button:
	summerized_prompt = Summerize(prompt,dropdown)
	result = summerized_prompt.generate_paragraph()
	st.write(result)
	st.success("Summarization successfully completed")