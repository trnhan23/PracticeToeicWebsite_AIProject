**# PracticeToeicWebsite_AIProject**

**1. Clone Repository**
Trước tiên, clone project về máy.

**2. Tạo Môi Trường Ảo**
_Trên Windows (cmd/Powershell):_
Khuyến khích sử dụng môi trường ảo để cài đặt các dependencies, cách tạo:

python -m venv env (để tạo môi trường ảo có tên env) 
env\Scripts\activate (để vào môi trường ảo)

**3. Cài Đặt Dependencies**
Sau khi kích hoạt môi trường ảo, cài đặt các thư viện từ file requirements.txt

Cài đặt ffmpeg:
Tải ffmpeg từ link: https://ffmpeg.org/download.html
Giải nén và đặt vào folder môi trường "env"

**4. Chạy Project**
Sử dụng lệnh sau để khởi chạy:
uvicorn app.main:app --host 0.0.0.0 --port 5050 --reload

------
Chúc bạn code vui vẻ! 🚀

