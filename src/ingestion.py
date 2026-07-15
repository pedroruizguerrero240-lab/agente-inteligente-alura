import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Definimos la ruta del archivo
caminho_pdf = "data/base_conocimiento_logistica.pdf"

# 2. Cargamos el documento
print("Cargando documento...")
loader = PyPDFLoader(caminho_pdf)
documentos = loader.load()

# 3. Dividimos el texto en fragmentos (chunks)
print("Dividiendo documento...")
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
documentos_divididos = splitter.split_documents(documentos)

print(f"Documento procesado. Se generaron {len(documentos_divididos)} fragmentos.")