# Agente Inteligente de Logística - LogiExpress S.A.

Este proyecto consiste en un agente inteligente diseñado para automatizar y optimizar la atención al cliente de **LogiExpress S.A.**, desarrollado como parte del programa **Oracle Next Education**.

## 🚀 Descripción del Proyecto
El agente utiliza procesamiento de lenguaje natural (NLP) y técnicas de búsqueda vectorial para responder consultas de usuarios sobre procesos logísticos, estado de envíos y políticas de servicio de manera precisa y eficiente.

## 🛠️ Tecnologías Utilizadas
*   **Lenguaje:** Python 3.14
*   **Framework de IA:** LangChain
*   **Base de Datos Vectorial:** FAISS
*   **Modelos de Embeddings:** Cohere (multilingual-v3.0)
*   **Frontend:** Streamlit
*   **Despliegue:** Streamlit Cloud

## 📂 Estructura del Repositorio
*   `/src`: Contiene la lógica central del agente (consulta, ingesta y configuración).
*   `/db`: Almacenamiento de la base de datos vectorial (índices FAISS).
*   `/data`: Documentación base para la ingesta de conocimiento.
*   `app.py`: Interfaz principal de la aplicación.

## ⚙️ Configuración y Despliegue
Para ejecutar este proyecto localmente, asegúrese de configurar su entorno:

1.  **Clonar el repositorio:**
    `git clone https://github.com/pedroruizguerrero240-lab/agente-inteligente-alura.git`
2.  **Instalar dependencias:**
    `pip install -r requirements.txt`
3.  **Configurar Variables de Entorno:**
    Cree un archivo `.env` en la raíz con su `COHERE_API_KEY`.
4.  **Ejecutar:**
    `streamlit run app.py`

## 👤 Autor
**Pedro Ruiz**  
Estudiante de Ingeniería en Ciencias de la Computación | ESPOL  
[Enlace a mi GitHub](https://github.com/pedroruizguerrero240-lab)
