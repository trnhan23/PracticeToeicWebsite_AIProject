import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Định nghĩa đường dẫn
TEMP_DIR = os.path.join(BASE_DIR, "uploads")
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")

# Định nghĩa mô hình TTS & Whisper
TTS_MODEL_PATH = "tts_models/en/ljspeech/tacotron2-DDC"
WHISPER_MODEL_PATH = "tiny.en"

# FFMPEG PATH
FFMPEG_PATH = os.path.join(os.path.dirname(BASE_DIR), "env", "ffmpeg", "bin")
os.environ["PATH"] = FFMPEG_PATH + os.pathsep + os.environ["PATH"]
