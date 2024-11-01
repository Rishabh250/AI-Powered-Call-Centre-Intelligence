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

# Function to generate a response using Google Gemini's API
def generate_response(customer_query):
    response = chat_model.generate_response(prompt=customer_query, max_tokens=100)
    return response.strip()

# Define API endpoint
@app.route('/api/customer_interaction', methods=['POST'])
def customer_interaction():
    data = request.json
    customer_query = data.get('query')
    response_text = generate_response(customer_query)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(port=5000, debug=True) 