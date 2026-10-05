from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

chave = os.environ.get("GEMINI_API_KEY")
cliente = genai.Client(api_key=chave)

SYSTEM_PROMPT = """ 
Voê é o atendente da Barbearia LaVi.

INFORMAÇÕES DA BARBEARIA:
Nome: Barbearia LaVi
Endereço: Basilio vila rios, 364 -Leme sp
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
SE NÃO SOUBER A RESPOSTA, DIGA "VOU VERIFICAR COM A EQUIPE E TE RETORNO"
NUNCA INVENTE INFORMAÇÕES
RESPOSTAS CURTAS E DIRETAS
SEMPRE PERGUNTE SE O CLIENTE QUER AGENDAR
"""
nome = input("Qual é o seu nome? ")

while True:
    pergunta = input(f"{nome}, o que deseja saber? ")

    if pergunta =="sair":
        print(f"Até logo, {nome}!")
        break

    resposta = cliente.models.generate_content(
   model="gemini-3.6-flash",
         contents=f"{SYSTEM_PROMPT}\n\nCliente {nome} perguntou: {pergunta}"
    )

    print(f"\n{resposta.text}\n")