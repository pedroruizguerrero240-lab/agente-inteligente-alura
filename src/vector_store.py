import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from ingestion import documentos_divididos

# Cargar variables del archivo .env
load_dotenv()

# 1. Configuramos el modelo de embeddings de Google
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# 2. Creamos la base de datos vectorial FAISS
print("Creando base de datos vectorial...")
db = FAISS.from_documents(documentos_divididos, embeddings)

# 3. Guardamos la base de datos localmente
db.save_local("db/faiss_index")
print("Base de datos guardada en la carpeta 'db/faiss_index'.")