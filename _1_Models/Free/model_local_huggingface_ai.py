import os
from pathlib import Path

BASE_DIR = Path.cwd() / "my_models"
BASE_DIR.mkdir(parents=True, exist_ok=True)  # Create dir if not exists

os.environ["HF_HOME"] = str(BASE_DIR)
os.environ["HF_HUB_CACHE"] = str(BASE_DIR / "hub")
os.environ["TRANSFORMERS_CACHE"] = str(BASE_DIR / "transformers")

# ✅ Verify paths before proceeding
print(f"Models will download to: {os.environ['HF_HOME']}")

from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

llm = HuggingFacePipeline.from_model_id( # type: ignore
    model_id="HuggingFaceTB/SmolLM2-135M-Instruct",
    task="text-generation",
     pipeline_kwargs=dict(
        do_sample=False,
        temperature=0.7,
        repetition_penalty=1.03,
    ),
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is AI?")

print(response.content) # type: ignore