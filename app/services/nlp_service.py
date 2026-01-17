import re

# Simple medical keyword maps
RISK_KEYWORDS = {
    "diabetes": ["glucose", "sugar", "hyperglycemia", "insulin"],
    "cholesterol": ["cholesterol", "ldl", "hdl", "triglycerides"],
    "blood_pressure": ["blood pressure", "hypertension", "bp"],
    "heart": ["heart", "cardiac", "cholesterol"],
}

SEVERITY_WORDS = ["high", "elevated", "severe", "critical", "abnormal"]


def analyze_text_report(report_text: str):
    text = report_text.lower()

    detected_conditions = []
    risk_factors = []
    severity = "normal"

    # Detect medical conditions
    for condition, keywords in RISK_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                detected_conditions.append(condition)
                break

    # Detect severity
    for word in SEVERITY_WORDS:
        if word in text:
            severity = "elevated"
            break

    # Basic recommendations
    recommendations = []
    if "diabetes" in detected_conditions:
        recommendations.append("Monitor blood glucose levels regularly.")
        recommendations.append("Consider HbA1c testing.")

    if "cholesterol" in detected_conditions:
        recommendations.append("Adopt a low-fat diet.")
        recommendations.append("Regular lipid profile testing recommended.")

    if "blood_pressure" in detected_conditions:
        recommendations.append("Monitor blood pressure daily.")
        recommendations.append("Reduce salt intake.")

    if not recommendations:
        recommendations.append("No critical issues detected. Maintain a healthy lifestyle.")

    return {
        "summary": "Medical report analyzed successfully",
        "severity": severity,
        "detected_conditions": list(set(detected_conditions)),
        "recommendations": recommendations,
    }
