import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Definimos la ruta de forma absoluta y segura
# __file__ es este archivo (ingestion.py)
# subimos un nivel (..) para salir de 'src' y bajamos a 'data'
base_dir = os.path.dirname(os.path.abspath(__file__))
caminho_pdf = os.path.join(base_dir, "..", "data", "base_conocimiento_logistica.pdf")

print(f"Cargando documento desde: {caminho_pdf}")

# 2. Cargamos el PDF
loader = PyPDFLoader(caminho_pdf)
documentos = loader.load()

# 3. Dividimos el texto en fragmentos
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
documentos_divididos = text_splitter.split_documents(documentos)

print(f"Documento dividido en {len(documentos_divididos)} fragmentos.")