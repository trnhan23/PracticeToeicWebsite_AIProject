import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.text_to_speech import router as tts_router
from app.api.routes.transcribe import router as transcribe_router

app = FastAPI()

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# Đăng ký các route
app.include_router(transcribe_router, prefix="/transcribe", tags=["Transcription"])
app.include_router(tts_router, prefix="/text-to-speech", tags=["Text-to-Speech"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)
