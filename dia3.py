from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

chave = os.environ.get("GEMINI_API_KEY")
cliente = genai.Client(api_key=chave)

nome = input("Qual é o seu nome? ")

while True:
    pergunta = input(f"{nome}, o que deseja saber? ")

    if pergunta =="sair":
        print(f"Até logo, {nome}!")
        break

    resposta = cliente.models.generate_content(
   model="gemini-3.6-flash",
        contents=f"Você é um atendente de barbearia. Responda de forma direta e simpática: {pergunta}"
    )
    print(f"\n{resposta.text}\n")