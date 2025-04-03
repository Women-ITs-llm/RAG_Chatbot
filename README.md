# RAG_Chatbot
국가법령정보센터의 법령을 이용한 챗봇 구현

## 환경설정
### Conda 가상환경 생성
```bash
conda create -n women_its python=3.10
conda activate women_its
```

### Package & Module 설치
```bash
pip install -r requirements.txt
```

### .env 파일 포맷
```bash
# OpenRouter API Key
OPENROUTER_API_KEY=sk-or-v1-abcd

# DB 설정
POSTGRES_USER=women_its
POSTGRES_PASSWORD=women_its
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=postgres
```

### PGVector Docker
Docker Desktop 설치

PGVector Docker Compose
```bash
docker-compose up -d
```