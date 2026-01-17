import requests

API_URL = "http://api:8000"

def predict_disease(payload):
    response = requests.post(f"{API_URL}/predict", json=payload)
    return response.json()

def analyze_report(payload):
    response = requests.post(f"{API_URL}/analyze-report", json=payload)
    return response.json()
