from fastapi import APIRouter
from pydantic import BaseModel
from app.services.textToSpeechService import generate_speech

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/")
async def text_to_speech(input_data: TextInput):
    return await generate_speech(input_data.text)
