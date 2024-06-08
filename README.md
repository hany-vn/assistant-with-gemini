# Dự Án Tạo và Phát Nhận Dạng Giọng Nói

## Mô tả
Dự án này sử dụng thư viện SpeechRecognition để nhận dạng giọng nói từ người dùng và thư viện gTTS (Google Text-to-Speech) để tạo và phát ra giọng nói tổng hợp. Nó cũng sử dụng các thư viện khác như playsound để phát âm thanh, và google.generativeai để thực hiện một số tác vụ AI khác.

## Yêu Cầu Hệ Thống
- Python 3.x
- Cài đặt các thư viện được liệt kê trong tệp requirements.txt bằng lệnh: `pip install -r requirements.txt`
- Kết nối Internet để sử dụng các dịch vụ của Google Text-to-Speech và Google Generative AI.

## Cài Đặt
1. Clone dự án từ repository GitHub: `git clone https://github.com/hany-vn/assistant-with-gemini`
2. Di chuyển vào thư mục dự án: `cd your_project`
3. Cài đặt các thư viện cần thiết: `pip install -r requirements.txt`

## Sử Dụng
1. Chạy file `main.py` để khởi động ứng dụng.
2. Ứng dụng sẽ chờ đợi người dùng nói một câu.
3. Sau khi người dùng nói xong, ứng dụng sẽ nhận dạng câu nói và phát ra giọng nói tổng hợp của nó.

## Tùy Chỉnh
- Bạn có thể thay đổi ngôn ngữ nhận dạng và ngôn ngữ tổng hợp giọng nói bằng cách sửa đổi các tham số trong file `main.py`.
- Bạn cũng có thể thay đổi tốc độ của giọng nói bằng cách chỉnh sửa tham số `speed` trong hàm `gTTS()`.

## Cảnh Báo
- Sử dụng thư viện SpeechRecognition yêu cầu kết nối Internet để sử dụng các dịch vụ của Google. Hãy chắc chắn rằng máy tính của bạn có kết nối Internet khi chạy dự án.
- Để tránh bị chặn bởi các chính sách bảo mật của Google, hãy sử dụng dịch vụ GTTS một cách có trách nhiệm và tuân thủ các hướng dẫn và điều khoản sử dụng của Google Text-to-Speech.

## Tác Giả
Tên Dự Án được phát triển bởi [Hany](https://github.com/hany-vn).
