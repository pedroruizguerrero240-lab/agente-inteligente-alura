import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from ingestion import documentos_divididos

# Cargar variables del archivo .env
load_dotenv()

# 1. Configuramos el modelo de embeddings de Cohere
# Usamos el modelo 'multilingual' para asegurar soporte completo
embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")

# 2. Creamos la base de datos vectorial FAISS
print("Creando base de datos vectorial con Cohere...")
db = FAISS.from_documents(documentos_divididos, embeddings)

# 3. Guardamos la base de datos localmente
db.save_local("db/faiss_index")
print("Base de datos creada y guardada en la carpeta 'db/faiss_index'.")