from dotenv import load_dotenv
from groq import Groq

load_dotenv()





def take_prompt(prompt: str):
    client = Groq()

    chat_completion = client.chat.completions.create(
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": f"{prompt}",
        }
    ],

    # The language model which will generate the completion.
    model="qwen/qwen3.8-27b"
    )

    # Print the completion returned by the LLM.
    print(chat_completion.choices[0].message.content)


bad_prompt = """
Laptop not working
"""


good_prompt = """
Based on the 6-section anatomy discussed in the video, here is the production-grade prompt template. You can fill in the bracketed placeholders for your specific use case:

**Role:** You are a [role, e.g., support assistant at a laptop company].

**Task:** Your task is to [clear action, e.g., classify the provided user issue].

**Constraints:** Follow these rules: [e.g., Only classify into these categories: Billing, Technical, Return].

**Output Format:** [e.g., Provide the response in one word only, matching the exact category name].

**Examples:**

-   Input: [e.g., My laptop screen is flickering.]
-   Output: Technical

**Fallback:** If the input is unrelated to the categories, output: [e.g., Other].

my marrage is broke
"""

# take_prompt(bad_prompt)
take_prompt(good_prompt)