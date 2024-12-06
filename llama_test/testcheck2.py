from transformers import LlamaTokenizer, LlamaForCausalLM
import torch

# LLAMA 모델 및 토크나이저 경로
MODEL_PATH = "C:/Users/cmzkep/.llama/checkpoints/Llama3.2-11B-Vision/consolidated.00.pth"
TOKENIZER_PATH = "C:/Users/cmzkep/.llama/checkpoints/Llama3.2-11B-Vision/tokenizer.model"

# LlamaTokenizer를 로컬 파일에서 로드
tokenizer = LlamaTokenizer(vocab_file=TOKENIZER_PATH)

# PyTorch 모델 로드
model = LlamaForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float16)

# 입력 데이터 생성
input_text = "What is the capital of France?"
inputs = tokenizer(input_text, return_tensors="pt")

# 모델로 텍스트 생성
outputs = model.generate(**inputs)

# 결과 출력
print(tokenizer.decode(outputs[0], skip_special_tokens=True))