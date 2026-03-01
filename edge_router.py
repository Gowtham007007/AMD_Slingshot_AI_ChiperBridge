from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# The IP address of your 16GB PC running the AI Backend
CORE_BACKEND_URL = "http://192.168.1.YY:8000/ai_analyze"
VALID_TOKEN = "AMD-EDU-AUTH-99283A"

@app.route('/route', methods=['POST'])
def route_traffic():
    # 1. Zero-Trust Token Check
    auth_header = request.headers.get('Authorization')
    if auth_header != VALID_TOKEN:
        print("[BLOCKED] Invalid Auth Token. Dropping connection.")
        return jsonify({"status": "Access Denied"}), 401

    # 2. Extract Encrypted/Raw Payload
    payload = request.json
    print(f"[ROUTING] Secure payload received from {payload.get('device_id')}. Forwarding to Core Backend...")

    # 3. Forward to the PC AI Engine
    try:
        response = requests.post(CORE_BACKEND_URL, json=payload, timeout=3)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("[ERROR] Core Backend Unreachable.")
        return jsonify({"status": "Backend Offline"}), 503

if __name__ == '__main__':
    # Run on all network interfaces on port 5000
    app.run(host='0.0.0.0', port=5000)
