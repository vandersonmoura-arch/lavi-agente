from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

app = FastAPI()

cliente = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
Você é o atendente virtual da Barbearia LaVi.

INFORMAÇÕES:
- Horário: Segunda a sábado das 9h às 19h
- Domingo: FECHADO

SERVIÇOS E PREÇOS:
- Corte: R$ 35
- Barba: R$ 25
- Corte + Barba: R$ 55
- Hidratação: R$ 40

PAGAMENTO:
- Dinheiro e Pix apenas

REGRAS:
- Nunca invente informações
- Respostas curtas e diretas
"""

class Mensagem(BaseModel):
    nome: str
    texto: str

@app.get("/")
def inicio():
    return {"mensagem": "Agente LaVi online"}

@app.post("/conversar")
def conversar(mensagem: Mensagem):
    contexto = f"{SYSTEM_PROMPT}\n\nCliente {mensagem.nome} perguntou: {mensagem.texto}"
    
    resposta = cliente.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=contexto
    )
    
    return {
        "usuario": mensagem.nome,
        "resposta": resposta.text
    }