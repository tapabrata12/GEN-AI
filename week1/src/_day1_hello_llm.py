from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

try:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if not GROQ_API_KEY:
        raise KeyError("GROQ_API_KEY is not set in the environment variables")
except KeyError:
    raise KeyError("API key is not available")

client = Groq(api_key= GROQ_API_KEY)

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ],
    model="openai/gpt-oss-20b"
)

print(chat_completion.choices[0].message.content)