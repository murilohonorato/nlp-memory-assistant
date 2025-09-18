# backend/app.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="NLP Memory Assistant - Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatReq(BaseModel):
    user_id: str
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat(req: ChatReq):
    # placeholder: eco da mensagem
    return {"reply": f"Você disse: {req.message}", "mem_used": []}

