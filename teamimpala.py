import streamlit as st
import random
import time

# =============================
# CONFIGURACIÓN DE LA PÁGINA
# =============================
st.set_page_config(
    page_title="Trivia Tame Impala",
    page_icon="🎸",
    layout="centered"
)

# =============================
# ESTILOS VISUALES
# =============================
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #8E24AA;
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
        border-ra
