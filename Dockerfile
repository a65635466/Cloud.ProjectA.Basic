# Python 3.13 공식 이미지 사용
From python:3.13-slim

# 작업 폴더 생성
WORKDIR /app

# requirements 먼저 복사
COPY requirements.txt .

# 필요한 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 전체 복사
COPY . .

# Flask 포트
EXPOSE 5000

# 실행 명령
CMD ["python", "app.py"]