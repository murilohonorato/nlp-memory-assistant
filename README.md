# NLP Memory Assistant - Protótipo (Windows friendly)

Protótipo de assistente conversacional com memória persistente.

## Como rodar (Windows - PowerShell)
1. Clonar repo (ou criar via GitHub Web)
2. python -m venv .venv
3. .\.venv\Scripts\Activate.ps1
4. pip install -r requirements.txt
5. cd backend; uvicorn app:app --reload --port 8000
6. em outra janela: streamlit run frontend/app.py

Endpoints:
- GET /health
- POST /chat  { "user_id": "...", "message": "..." }
