import streamlit as st
from Prompt import Summerize
# Summarizer
st.title("Chat AI No Memory")

prompt = st.text_input("Enter the your Query: ")
button = st.button("Send")
if button:
        summerized_prompt = Summerize(prompt)
        result = summerized_prompt.generate_paragraph()
        st.write(result)
    