from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

cliente = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

for modelo in cliente.models.list():
    print(modelo.name)
