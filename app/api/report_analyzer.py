from fastapi import APIRouter
from pydantic import BaseModel
from app.services.nlp_service import analyze_text_report

router = APIRouter()

class ReportInput(BaseModel):
    report_text: str

@router.post("/analyze-report")
def analyze_report(data: ReportInput):
    return analyze_text_report(data.report_text)
