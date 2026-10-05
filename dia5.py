from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

chave = os.environ.get("GEMINI_API_KEY")
cliente = genai.Client(api_key=chave)
SYSTEM_PROMPT = """
Voê é o atendente da Barbearia LaVi.

INFORMAÇÕES DA BARBEARIA:
Horário: Segunda a sábado: 9h às 19h
Domingo: FECHADO

SERVIÇOS E PREÇOS:
Corte: R$35
Barba: R$25
Corte e Barba: R$55
Hidratação: R$40

FORMAS DE PAGAMENTO:
DINHEIRO E PIX APENAS
Não aceitamos cartões de crédito ou débito.

REGRAS IMPORTANTES:
Nunca invente informações
Respostas curtas e diretas
Se não souber a resposta, diga "VOU VERIFICAR COM A EQUIPE E TE RETORNO"
"""

historico = []

nome = input("Qual é o seu nome? ")
print(f"\nOlá, {nome}! Bem-vindo à Barbearia LaVi. Como posso ajudá-lo hoje?")

historico.append(f"Cliente se apresentou: {nome}.")

while True:
    pergunta = input(f"\n{nome}, o que deseja saber? ")

    if pergunta == "sair":
        print(f"Ate logo, {nome}!")
        break

    historico.append(f"Cliente: {pergunta}")

    contexto = SYSTEM_PROMPT + "\n\nHistorico da conversa:\n" + "\n".join(historico)

    resposta = cliente.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=contexto
    )

    historico.append(f"Atendente: {resposta.text}")

    print(f"\n{resposta.text}")