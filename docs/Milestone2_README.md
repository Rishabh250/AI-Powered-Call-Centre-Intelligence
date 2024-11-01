# Milestone 2: Agent Assistance System

## Overview
This milestone focuses on creating a real-time assistance feature that offers agents context-aware suggestions using OpenAI.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure OpenAI API Key**:
   - Set `OPENAI_API_KEY` in your environment.

4. **Run the API**:
   ```bash
   python src/agent_assistance/api.py
   ```

## API Details

- **Endpoint**: `POST /api/agent_assistance`
- **Request Body**: `{ "query": "The customer wants a refund", "session_id": "12345" }`
- **Response**: `{ "suggestion": "Advise the customer that the refund process will take 3-5 business days." }`

## Testing

- Run unit tests:
  ```bash
  python -m unittest discover src/agent_assistance/tests
  ``` 