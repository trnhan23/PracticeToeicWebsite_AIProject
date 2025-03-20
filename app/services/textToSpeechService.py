import os
from datetime import datetime
from fastapi.responses import FileResponse
from TTS.api import TTS
from app.core.constants import DOWNLOADS_DIR, TTS_MODEL_PATH

# Load mô hình TTS
tts_model = TTS(TTS_MODEL_PATH)

async def generate_speech(text: str):
    try:
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(DOWNLOADS_DIR, f"{timestamp}.wav")

        # Tạo file âm thanh
        tts_model.tts_to_file(text=text, file_path=output_path)
        return FileResponse(output_path, media_type="audio/wav", filename=f"{timestamp}.wav")

    except Exception as e:
        return {"errStatus": 1, "error": str(e)}
