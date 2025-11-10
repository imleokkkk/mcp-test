# Python 3.14 베이스 이미지 사용
FROM python:3.14-slim

# 작업 디렉토리 설정
WORKDIR /app

# uv 설치 (빠른 Python 패키지 관리자)
RUN pip install --no-cache-dir uv

# 의존성 파일 복사
COPY pyproject.toml uv.lock ./

# uv를 사용하여 의존성 설치
RUN uv pip install --system -r pyproject.toml

# 애플리케이션 소스 코드 복사
COPY . .

# 포트 노출 (FastMCP 서버가 8080 포트 사용)
EXPOSE 8080

# 서버 실행
CMD ["python", "server.py"]

