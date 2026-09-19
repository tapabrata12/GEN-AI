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


prompt1  = "Hello!"
prompt2 = "How are you?"
prompt3 = "Explain what is AI?"

messages = []
for prompt in [prompt1, prompt2, prompt3]:
    messages.append({"role": "user", "content": prompt})

chat_completion = client.chat.completions.create(messages=messages, model="openai/gpt-oss-20b")

print(chat_completion.choices[0].message.content)
usage = chat_completion.usage

print(f"Input tokens:{usage.prompt_tokens}")
print(f"Output tokens:{usage.completion_tokens}")
print(f"Total tokens:{usage.total_tokens}")