# Milestone 1: Initial Setup and Customer Interaction API

## Overview
This milestone involves setting up the development environment and implementing a basic Customer Interaction API using Google Gemini to handle common customer queries.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone  https://github.com/Rishabh250/AI-Powered-Call-Centre-Intelligence.git
   cd AI-Powered-Call-Centre-Intelligence
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Set `GOOGLE_API_KEY` for Google Gemini.
   - Set `GOOGLE_GENAI_MODEL` for the model name.
   - Set `MODEL_TEMPERATURE` for the model's temperature setting.

4. **Run the API**:
   ```bash
   python src/customer_interaction/api.py
   ```

## API Details

- **Endpoint**: `POST /api/customer_interaction`
- **Request Body**: `{ "query": "What is the status of my order?" }`
- **Response**: `{ "response": "Your order is being processed and will arrive shortly." }`

## Testing

- Run unit tests:
  ```bash
  python -m unittest discover src/customer_interaction/tests
  ``` 