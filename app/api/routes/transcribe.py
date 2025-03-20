from fastapi import APIRouter, UploadFile, File
from app.services.transcribeService import transcribe_audio

router = APIRouter()

@router.post("/")
async def transcribe(file: UploadFile = File(...)):
    return await transcribe_audio(file)
