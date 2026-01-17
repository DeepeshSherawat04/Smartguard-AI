from fastapi import FastAPI
from app.api.predict import router as predict_router
from app.api.report_analyzer import router as report_router

app = FastAPI(
    title="SMARTGUARD-AI",
    description="AI-powered preventive healthcare system",
    version="1.0.0"
)

app.include_router(predict_router)
app.include_router(report_router)

@app.get("/")
def root():
    return {"message": "SMARTGUARD-AI backend is running"}
