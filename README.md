# NLP Memory Assistant

Projeto pessoal para desenvolver um **assistente conversacional com memória de longo prazo**, usando **FastAPI (backend)** e **Streamlit (frontend)**.

## Como rodar no Windows

1. Criar ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
2. Instalar dependências:
   ```bash
   pip install -r requirements.txt
3. Rodar o backend:
   ```bash
   uvicorn backend.app:app --reload
    #Testar no navegador: http://localhost:8000/health
    #Deve mostrar: {"status":"ok"}.
4. Rodar o frontend:
    ```bash
    streamlit run frontend/app.py
    #Acessar no navegador: http://localhost:8501
