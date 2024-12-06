import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = "C:/Users/cmzkep/.llama/checkpoints/Llama3.2-11B-Vision/consolidated.00.pth"
TOKENIZER_PATH = "C:/Users/cmzkep/.llama/checkpoints/Llama3.2-11B-Vision/tokenizer.model"


tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float16)

input_text = "What is the capital of France?"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))