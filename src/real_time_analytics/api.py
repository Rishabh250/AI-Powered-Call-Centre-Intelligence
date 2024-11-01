from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# In-memory storage for analytics (for demo purposes)
analytics_data = []

@app.route('/api/analytics/log', methods=['POST'])
def log_interaction():
    data = request.json
    interaction_data = {
        "timestamp": time.time(),
        "query": data.get('query'),
        "response_time": data.get('response_time'),
        "outcome": data.get('outcome')
    }
    analytics_data.append(interaction_data)
    return jsonify({"status": "logged", "data": interaction_data})

@app.route('/api/analytics/retrieve', methods=['GET'])
def retrieve_analytics():
    return jsonify(analytics_data)

if __name__ == "__main__":
    app.run(port=5002, debug=True) 