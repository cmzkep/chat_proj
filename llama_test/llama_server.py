from flask import Flask, request, jsonify
from llama_cpp import Llama

# 모델 파일 경로
MODEL_PATH = "C:\\RYUN KIM\\.llama\\checkpoints\\Llama3.2-11B-Vision\\consolidated.00.pth"  # 실제 LLAMA 모델 파일 경로

# LLAMA 모델 로드
llm = Llama(model_path=MODEL_PATH)

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    # LLAMA 모델 응답 생성
    response = llm(question)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
