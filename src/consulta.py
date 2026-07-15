import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

# 1. Cargamos las variables de entorno
load_dotenv()

# 2. Configuramos el modelo de embeddings (el mismo usado en vector_store.py)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# 3. Cargamos nuestra base de datos local
db = FAISS.load_local("db/faiss_index", embeddings, allow_dangerous_deserialization=True)

# 4. Configuramos el modelo de lenguaje (el que dará las respuestas)
llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0)

# 5. Creamos el prompt que combina la pregunta con el contexto recuperado
prompt = ChatPromptTemplate.from_template("""
Responde la pregunta del usuario basándote únicamente en el siguiente contexto:

<context>
{context}
</context>

Pregunta: {input}
""")

# 6. Creamos la cadena que combina los documentos recuperados con el prompt
document_chain = create_stuff_documents_chain(llm, prompt)

# 7. Creamos la cadena de recuperación (retriever + document_chain)
retriever = db.as_retriever()
qa_chain = create_retrieval_chain(retriever, document_chain)

# 8. Modo interactivo: pregúntale lo que quieras
if __name__ == "__main__":
    print("🤖 Agente de logística listo. Escribe 'salir' para terminar.\n")
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() in ["salir", "exit", "quit"]:
            print("¡Hasta luego!")
            break
        respuesta = qa_chain.invoke({"input": pregunta})
        print(f"\nAgente: {respuesta['answer']}\n")