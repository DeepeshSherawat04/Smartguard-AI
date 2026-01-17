from fastapi import FastAPI, UploadFile
import easyocr
from transformers import pipeline
from PIL import Image
import io

app = FastAPI()

reader = easyocr.Reader(['en'], gpu=False)
nlp = pipeline("text-classification", model="distilbert-base-uncased")

@app.post("/analyze")
async def analyze(file: UploadFile):
    image = Image.open(io.BytesIO(await file.read()))
    text = " ".join(reader.readtext(image, detail=0))
    analysis = nlp(text[:512])
    return {"extracted_text": text, "analysis": analysis}
