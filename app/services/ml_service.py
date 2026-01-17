import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "disease_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_risk(features: list):
    data = np.array(features).reshape(1, -1)
    scaled_data = scaler.transform(data)

    probability = model.predict_proba(scaled_data)[0][1]

    if probability < 0.3:
        risk = "LOW"
    elif probability < 0.6:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return {
        "risk": risk,
        "probability": round(float(probability), 2)
    }
