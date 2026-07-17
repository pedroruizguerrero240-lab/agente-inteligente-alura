import streamlit as st
from src.consulta import obtener_respuesta 

# Configuración inicial
st.set_page_config(page_title="LOGIEXPRESS S.A.", page_icon="🚚", layout="centered")

# CSS personalizado para unificar tipografía y color
st.markdown("""
    <style>
    /* Ocultar elementos innecesarios */
    footer {visibility: hidden;}
    
    /* Fondo oscuro global */
    .stApp {background-color: #0e1117;}
    
    /* Unificar el color y legibilidad de todo el texto en la app */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stChatMessageContent {
        color: #E0E0E0 !important;
        font-size: 16px !important;
    }
    
    /* Asegurar que los encabezados resalten correctamente */
    h1 { color: #FFFFFF !important; }
    </style>
    """, unsafe_allow_html=True)

# Título y descripción
st.markdown("<h1 style='text-align: center;'>LOGIEXPRESS S.A.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1em;'>Asistente virtual especializado en gestión logística y soporte operativo.</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; border-top: 1px solid #333; margin: 20px 0;'>", unsafe_allow_html=True)

# Gestión del historial
if "messages" not in st.session_state:
    st.session_state.messages = []
    
    # Texto de bienvenida unificado
    bienvenida = """¡Hola! Soy tu asistente de LOGIEXPRESS S.A. 🚚. ¡Estoy listo para apoyarte!

Puedo ayudarte con información sobre estos temas:
* **Política de envíos**
* **Procedimiento de rastreo de pedidos**
* **Política de reembolsos y siniestros**
* **Preguntas frecuentes**
* **Proceso de reclamos y atención al cliente**

¿En qué puedo ayudarte hoy?"""
    
    st.session_state.messages.append({"role": "assistant", "content": bienvenida})

# Renderizado de mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Captura de input
if pregunta := st.chat_input("¿En qué puedo ayudarte con la logística de LOGIEXPRESS hoy?"):
    st.session_state.messages.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    with st.chat_message("assistant"):
        with st.spinner("Procesando información..."):
            respuesta = obtener_respuesta(pregunta)
            st.markdown(respuesta)
            
    st.session_state.messages.append({"role": "assistant", "content": respuesta})