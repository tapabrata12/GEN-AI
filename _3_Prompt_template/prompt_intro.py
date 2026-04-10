from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st


bmi_prompt = ChatPromptTemplate.from_messages([  # type: ignore
    ("system", """You are a precise health assistant. Calculate BMI and explain results clearly.
     Calculate the BMI using the following details:

Instructions:
1. Use the BMI formula: BMI = weight / (height^2)
2. Return the BMI value (rounded to 2 decimal places)
3. Classify into:
   - Underweight (<18.5)
   - Normal (18.5–24.9)
   - Overweight (25–29.9)
   - Obese (30+)
4. Give a short health interpretation

Output format:
BMI: <value>
Category: <category>
Advice: <short advice>
     """),
    
    ("human", 
     """
Calculate BMI for a person with weight {weight} kg and height {height} m.
""")
])

# UI
st.title("BMI Calculator")

weight = st.number_input("Enter weight (kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter height (m):", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        final_prompt = bmi_prompt.invoke({  # type: ignore
            "weight": weight,
            "height": height
        })

        llm = ChatGroq(
            model="qwen/qwen3-32b",
            temperature=0,
            max_tokens=None,
            reasoning_format="parsed",
            timeout=None,
            max_retries=2,
        )

        response = llm.invoke(final_prompt)

        st.text(response.content) # type: ignore
    else:
        st.warning("Please enter valid weight and height.")