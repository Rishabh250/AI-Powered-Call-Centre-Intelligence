# Milestone 3: Real-Time Analytics and Workflow Optimization

## Overview
This milestone involves implementing real-time analytics by capturing customer interaction data and calculating metrics to optimize workflows.

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

3. **Run the API**:
   ```bash
   python src/real_time_analytics/api.py
   ```

## API Details

- **POST** `/api/analytics/log`
  - **Request Body**: `{ "query": "Order status", "response_time": 1.2, "outcome": "resolved" }`
  - **Response**: `{ "status": "logged", "data": { ... } }`

- **GET** `/api/analytics/retrieve`
  - **Response**: `[ { "timestamp": 1630428380.0, "query": "Order status", "response_time": 1.2, "outcome": "resolved" }, ... ]`

## Testing

- Run unit tests:
  ```bash
  python -m unittest discover src/real_time_analytics/tests
  ``` 