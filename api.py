from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os
import logging


from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("agente-lavi")

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
    logger.info(f"Mensagem recebida de {mensagem.nome}: {mensagem.texto}")

    contexto = f"{SYSTEM_PROMPT}\n\nCliente {mensagem.nome} perguntou: {mensagem.texto}"

    try:
        resposta = cliente.models.generate_content(
           model="gemini-3.5-flash-lite",
            contents=contexto
        )
        logger.info(f"Resposta enviada para {mensagem.nome}")
        return {
            "usuario": mensagem.nome,
            "resposta": resposta.text
        }

    except Exception as erro:
        logger.error(f"Falha ao consultar a IA: {erro}")
        return {
            "usuario": mensagem.nome,
            "resposta": "Estamos com instabilidade no momento. Tente novamente em alguns minutos."
        }