from flask import Flask, request, jsonify
from sklearn.ensemble import IsolationForest
import numpy as np
import datetime

app = Flask(__name__)

# --- INITIALIZE THE AI MODEL ---
print("Initializing TrustAI Anomaly Detection Engine (Optimized for AMD)...")
ai_model = IsolationForest(contamination=0.1, random_state=42)

# Train the AI on what "normal" campus lab data looks like (Temperatures between 20C and 25C)
normal_data = np.array([[20.0], [21.5], [22.1], [23.8], [24.5], [25.0], [21.0], [22.9]])
ai_model.fit(normal_data)
print("TrustAI Engine Online and Monitoring.")

@app.route('/ai_analyze', methods=['POST'])
def analyze_data():
    data = request.json
    device_id = data.get('device_id')
    temp = float(data.get('Chemistry_Lab_Temp'))

    # --- AI INFERENCE ---
    # The AI scores the incoming temperature
    prediction = ai_model.predict(np.array([[temp]]))
    anomaly_score = ai_model.decision_function(np.array([[temp]]))[0]

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # -1 means Anomaly (Hacker / Sensor Malfunction)
    if prediction[0] == -1:
        print(f"\n[AI-ALERT] [{current_time}] TrustAI Score: {anomaly_score:.2f}")
        print(f"[BLOCKED] CRITICAL ANOMALY DETECTED in {device_id} (Temp: {temp}C). Connection Dropped.")
        print(f"[GEN-AI EXPLANATION] Alert: Abnormal data spike detected. Device {device_id} quarantined to protect campus intranet.\n")
        return jsonify({"status": "blocked", "reason": "AI anomaly detected"}), 403
    
    # 1 means Normal (Allow)
    else:
        print(f"[ALLOW] [{current_time}] TrustAI Score: {anomaly_score:.2f} -> Device {device_id} sent {temp}C safely.")
        return jsonify({"status": "allowed"}), 200

if __name__ == '__main__':
    # Run on the PC network interface on port 8000
    app.run(host='0.0.0.0', port=8000)
