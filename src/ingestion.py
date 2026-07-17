import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS

# Cargamos variables de entorno para la API KEY
load_dotenv()

# 1. Definimos las rutas
base_dir = os.path.dirname(os.path.abspath(__file__))
caminho_pdf = os.path.join(base_dir, "..", "data", "base_conocimiento_logistica.pdf")
db_path = os.path.join(base_dir, "..", "db", "faiss_index")

print(f"Cargando documento desde: {caminho_pdf}")

# 2. Cargamos el PDF
loader = PyPDFLoader(caminho_pdf)
documentos = loader.load()

# 3. Dividimos el texto
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documentos_divididos = text_splitter.split_documents(documentos)

print(f"Documento dividido en {len(documentos_divididos)} fragmentos.")

# 4. CONFIGURACIÓN COHERE (Asegúrese de tener COHERE_API_KEY en su .env)
print("Generando embeddings con Cohere...")
embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")

# 5. Guardado en FAISS (Esto sobrescribirá la versión vieja de HuggingFace)
db = FAISS.from_documents(documentos_divididos, embeddings)
db.save_local(db_path)

print(f"Base de datos vectorial creada y guardada en: {db_path}")