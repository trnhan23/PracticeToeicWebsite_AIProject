import os
import whisper
from app.core.constants import WHISPER_MODEL_PATH

# Load mô hình Whisper
model = whisper.load_model(WHISPER_MODEL_PATH)

async def transcribe_audio(file):
    try:
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            buffer.write(await file.read())

        # Chạy nhận diện giọng nói
        result = model.transcribe(temp_path)
        text = result["text"]
        
        os.remove(temp_path)
        return {"errStatus": 0, "text": text}

    except Exception as e:
        return {"errStatus": 1, "error": str(e)}
