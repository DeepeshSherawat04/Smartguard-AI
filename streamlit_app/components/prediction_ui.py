import streamlit as st
import requests

def render_prediction_ui():
    st.markdown("<h1>🩺 Disease Risk Prediction</h1>", unsafe_allow_html=True)
    st.markdown("Predict diabetes risk using clinical parameters.")

    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)

        pregnancies = col1.number_input("Pregnancies", 0, 20)
        glucose = col2.number_input("Glucose Level", 0, 300)
        bp = col3.number_input("Blood Pressure", 0, 200)

        skin = col1.number_input("Skin Thickness", 0, 100)
        insulin = col2.number_input("Insulin Level", 0, 900)
        bmi = col3.number_input("BMI", 0.0, 70.0)

        pedigree = col1.number_input("Diabetes Pedigree Function", 0.0, 3.0)
        age = col2.number_input("Age", 1, 120)

        submitted = st.form_submit_button("🔍 Predict Risk")

    if submitted:
        payload = {
            "pregnancies": pregnancies,
            "glucose": glucose,
            "blood_pressure": bp,
            "skin_thickness": skin,
            "insulin": insulin,
            "bmi": bmi,
            "diabetes_pedigree": pedigree,
            "age": age
        }

        try:
            res = requests.post("http://127.0.0.1:8000/predict", json=payload)
            data = res.json()

            st.success(f"Prediction: {data['prediction']}")
            st.metric("Risk Score", f"{data['risk_score']*100:.2f}%")

        except Exception:
            st.error("Backend not reachable.")
