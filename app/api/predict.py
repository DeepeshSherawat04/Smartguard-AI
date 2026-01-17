from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ml_service import predict_risk

router = APIRouter()

class HealthInput(BaseModel):
    pregnancies: int
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    diabetes_pedigree: float
    age: int

@router.post("/predict")
def predict_disease(data: HealthInput):
    features = [
        data.pregnancies,
        data.glucose,
        data.blood_pressure,
        data.skin_thickness,
        data.insulin,
        data.bmi,
        data.diabetes_pedigree,
        data.age
    ]

    result = predict_risk(features)

    recommendation = {
        "LOW": "Maintain a healthy lifestyle.",
        "MEDIUM": "Monitor health regularly and improve diet.",
        "HIGH": "Consult a doctor immediately."
    }

    return {
        "diabetes_risk": result["risk"],
        "probability": result["probability"],
        "recommendation": recommendation[result["risk"]]
    }
