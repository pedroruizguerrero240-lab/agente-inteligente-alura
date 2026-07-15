import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

try:
    genai.configure(api_key=api_key)
    # Intentamos listar modelos disponibles para ver si la conexión es real
    for m in genai.list_models():
        if 'embedContent' in m.supported_generation_methods:
            print(f"Modelo encontrado: {m.name}")
except Exception as e:
    print(f"Error de conexión: {e}")