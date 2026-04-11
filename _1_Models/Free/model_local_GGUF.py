import os
from pathlib import Path
from huggingface_hub import hf_hub_download # type: ignore
from langchain_community.llms import LlamaCpp


# 1. Setup Paths
BASE_DIR = Path.cwd() / "my_models"
BASE_DIR.mkdir(parents=True, exist_ok=True)

os.environ["HF_HOME"] = str(BASE_DIR)

print(f"Checking model in: {BASE_DIR}")

# 2. Download ONLY the specific 4-bit quantized file (Approx 4.7 GB)
# We use 'qwen2.5-coder-7b-instruct-q4_k_m.gguf' which is the best balance.
model_filename = "qwen2.5-coder-7b-instruct-q4_k_m.gguf"
repo_id = "Qwen/Qwen2.5-Coder-7B-Instruct-GGUF"

try:
    model_path = hf_hub_download(
        repo_id=repo_id,
        filename=model_filename,
        local_dir=BASE_DIR,
        local_dir_use_symlinks=False  # Downloads actual file to folder, not a symlink
    )
    print(f"✅ Model downloaded to: {model_path}")
except Exception as e:
    print(f"❌ Download failed: {e}")
    exit()

# 3. Load the Model using LlamaCpp (Optimized for GGUF)
# n_gpu_layers=-1 moves the whole model to your RTX 3050 (if installed with CUDA)
llm = LlamaCpp(
    model_path=str(model_path),
    n_gpu_layers=-1,      # -1 = offload all layers to GPU. Change to 0 if you only have CPU.
    n_batch=512,          # specific to llama.cpp
    n_ctx=4096,           # Context window
    temperature=0.7,
    verbose=True,
)

# 4. Run Inference
question = "Write a Python function to calculate the Fibonacci sequence."
print(f"\n🤖 Generating answer for: '{question}'...\n")

response = llm.invoke(question)

print("--- RESPONSE ---")
print(response)
