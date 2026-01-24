from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(model_provider="google_genai",model="gemini-3-flash-preview", temperature=0.7)

result = model.invoke("What is the capital of India ?")
print(result.content)