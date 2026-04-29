import streamlit as st
import random
import time

# =============================
# CONFIGURACIÓN DE LA PÁGINA
# =============================
st.set_page_config(
    page_title="Trivia Verbo To Be",
    page_icon="⭐",
    layout="centered"
)

# =============================
# ESTILOS VISUALES
# =============================
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #6A1B9A;
        font-size: 42px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 18px;
        margin-bottom: 25px;
    }
    .correct-box {
        background-color: #E8F5E9;
        border-left: 6px solid #43A047;
        padding: 15px;
        border-radius: 10px;
        color: #1B5E20;
        font-weight: bold;
        margin-top: 15px;
    }
    .wrong-box {
        background-color: #FFEBEE;
        border-left: 6px solid #E53935;
        padding: 15px;
        border-radius: 10px;
        color: #B71C1C;
        font-weight: bold;
        margin-top: 15px;
    }
    .stars {
        text-align: center;
        font-size: 42px;
        animation: sparkle 1s infinite alternate;
        margin-top: 20px;
    }
    @keyframes sparkle {
        from { transform: scale(1); opacity: 0.6; }
        to { transform: scale(1.25); opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# =============================
# BANCO DE PREGUNTAS
# =============================
preguntas = [
    {
        "pregunta": "Complete la oración: I ___ a student.",
        "opciones": ["am", "is", "are", "be"],
        "respuesta": "am"
    },
    {
        "pregunta": "Complete la oración: She ___ my friend.",
        "opciones": ["is", "am", "are", "be"],
        "respuesta": "is"
    },
    {
        "pregunta": "Complete la oración: They ___ happy.",
        "opciones": ["are", "is", "am", "be"],
        "respuesta": "are"
    },
    {
        "pregunta": "¿Cuál es la forma negativa correcta de: He is tall?",
        "opciones": ["He is not tall", "He are not tall", "He am not tall", "He be not tall"],
        "respuesta": "He is not tall"
    },
    {
        "pregunta": "¿Cuál e
