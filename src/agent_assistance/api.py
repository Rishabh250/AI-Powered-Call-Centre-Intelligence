from flask import Flask, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Initialize Flask app
app = Flask(__name__)

# Configure Google Gemini API key and model parameters
google_api_key = os.getenv("GOOGLE_API_KEY")
model_name = os.getenv("GOOGLE_GENAI_MODEL")
temperature = float(os.getenv("MODEL_TEMPERATURE", 0.7))

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

# Initialize Google Gemini chat model
chat_model = ChatGoogleGenerativeAI(
    google_api_key=google_api_key,
    model=model_name,
    temperature=temperature
)

# Memory cache to maintain conversation context
memory_cache = {}

def get_assistant_suggestion(query, session_id):
    # Retrieve session context or initialize
    context = memory_cache.get(session_id, "")
    prompt = f"{context}\nUser: {query}\nAgent:"
    
    response = chat_model.generate_response(prompt=prompt, max_tokens=100)
    memory_cache[session_id] = f"{context}\nUser: {query}\nAgent: {response.strip()}"
    return response.strip()

@app.route('/api/agent_assistance', methods=['POST'])
def agent_assistance():
    data = request.json
    query = data.get('query')
    session_id = data.get('session_id')
    suggestion = get_assistant_suggestion(query, session_id)
    return jsonify({"suggestion": suggestion})

if __name__ == "__main__":
    app.run(port=5001, debug=True) 