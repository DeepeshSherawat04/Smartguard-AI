🩺 SMARTGUARD-AI
AI-Powered Preventive Healthcare System

SMARTGUARD-AI is an end-to-end AI-driven preventive healthcare application that predicts disease risk and analyzes medical reports using Machine Learning, NLP, FastAPI, and Streamlit.

The system is designed to demonstrate real-world AI engineering practices, clean architecture, and user-friendly medical dashboards.

🚀 Key Features
🔍 Disease Risk Prediction

Predicts diabetes risk using clinical parameters

ML model trained on Pima Indians Diabetes Dataset

Risk classification: Low / Medium / High

JSON-based inference via FastAPI

📝 Medical Report Analysis (NLP)

Analyzes medical text reports

Extracts key health indicators (e.g., glucose, cholesterol)

NLP-powered insights using Transformers (rule-based fallback supported)

📊 Interactive Streamlit Dashboard

Clean and modern UI

Sidebar navigation (Dashboard / Prediction / Report Analysis)

Real-time backend integration

User-friendly error handling

🏗️ System Architecture
User (Browser)
     |
     v
Streamlit Dashboard (Frontend)
     |
     v
FastAPI Backend (REST APIs)
     |
     v
ML Model (.pkl) + NLP Service

🧠 Tech Stack
Backend

FastAPI

Uvicorn

Scikit-learn

Joblib

Machine Learning

Logistic Regression

Feature Scaling (StandardScaler)

Trained .pkl model

NLP

Transformers (optional)

Rule-based medical keyword analysis

SentencePiece support

Frontend

Streamlit

Requests

Modular UI components

📂 Project Structure
SMARTGUARD-AI/
│
├── app/
│   ├── api/
│   │   ├── predict.py
│   │   └── report_analyzer.py
│   │
│   ├── services/
│   │   ├── ml_service.py
│   │   └── nlp_service.py
│   │
│   ├── models/
│   │   ├── disease_model.pkl
│   │   └── scaler.pkl
│   │
│   └── main.py
│
├── ml/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
│
├── streamlit_app/
│   ├── dashboard.py
│   └── components/
│       ├── prediction_ui.py
│       └── report_ui.py
│
├── requirements.txt
└── README.md

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/DeepeshSherawat04/Smartguard-AI.git
cd SMARTGUARD-AI

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Application
Start FastAPI Backend
uvicorn app.main:app --reload --port 8000


Open Swagger UI:

http://127.0.0.1:8000/docs

Start Streamlit Frontend (New Terminal)
streamlit run streamlit_app/dashboard.py


Open Dashboard:

http://localhost:8501

🔌 API Endpoints
🔹 Predict Disease Risk

POST /predict

{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 80,
  "BMI": 28.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 35
}

🔹 Analyze Medical Report

POST /analyze-report

{
  "report_text": "Patient glucose levels are high and cholesterol is elevated."
}

🧪 Model Training (Optional)

To retrain the ML model:

cd ml
python train.py


This regenerates:

disease_model.pkl

scaler.pkl

🎯 Use Cases

Preventive healthcare screening

AI healthcare demos & portfolios

ML + FastAPI + Streamlit reference project

Academic / interview-ready project

⚠️ Disclaimer

SMARTGUARD-AI is for educational and demonstration purposes only.
It is not a substitute for professional medical diagnosis or treatment.

👨‍💻 Author

Deepesh Sherawat
AI / Software Engineer
Project: SMARTGUARD-AI