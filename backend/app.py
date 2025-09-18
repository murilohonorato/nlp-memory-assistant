from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="NLP Memory Assistant - Backend")

# Configuração de CORS (necessário para o frontend acessar o backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados da requisição
class ChatRequest(BaseModel):
    user_id: str
    message: str

# Endpoint de saúde
@app.get("/health")
def health():
    return {"status": "ok"}

# Endpoint de chat
@app.post("/chat")
async def chat(req: ChatRequest):
    # placeholder: eco da mensagem
    return {"reply": f"Você disse: {req.message}", "mem_used": []}
