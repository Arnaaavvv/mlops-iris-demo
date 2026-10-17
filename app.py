from flask import Flask, request, jsonify
import joblib
import numpy as np
from datetime import datetime
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "iris_model.pkl")
LOG_FILE = os.path.join(os.path.dirname(__file__), "ml_api.log")

model = joblib.load(MODEL_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or 'features' not in data:
        return jsonify({'error': 'Please provide features'}), 400

    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)[0]

    log = {
        'timestamp': datetime.utcnow().isoformat(),
        'input': data['features'],
        'prediction': str(prediction)
    }

    with open(LOG_FILE, 'a') as f:
        f.write(str(log) + '\n')

    return jsonify({'prediction': str(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
