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
        "pregunta": "¿Cuál es la pregunta correcta?",
        "opciones": ["Are you ready?", "You are ready?", "Is you ready?", "Am you ready?"],
        "respuesta": "Are you ready?"
    }
]

# =============================
# ESTADO DE LA APP
# =============================
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0

if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0

if "respondido" not in st.session_state:
    st.session_state.respondido = False

if "opciones_mezcladas" not in st.session_state:
    st.session_state.opciones_mezcladas = random.sample(
        preguntas[0]["opciones"],
        len(preguntas[0]["opciones"])
    )

# =============================
# TÍTULO
# =============================
st.markdown('<div class="main-title">⭐ Trivia del Verbo To Be ⭐</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Responde 5 preguntas y practica el uso de am, is y are.</div>', unsafe_allow_html=True)

# =============================
# MOSTRAR PREGUNTA
# =============================
if st.session_state.pregunta_actual < len(preguntas):
    pregunta_data = preguntas[st.session_state.pregunta_actual]

    st.progress(st.session_state.pregunta_actual / len(preguntas))
    st.subheader(f"Pregunta {st.session_state.pregunta_actual + 1} de {len(preguntas)}")
    st.write(f"### {pregunta_data['pregunta']}")

    seleccion = st.radio(
        "Elige una alternativa:",
        st.session_state.opciones_mezcladas,
        key=f"respuesta_{st.session_state.pregunta_actual}"
    )

    if st.button("Responder") and not st.session_state.respondido:
        st.session_state.respondido = True

        if seleccion == pregunta_data["respuesta"]:
            st.session_state.puntaje += 1
            st.markdown('<div class="correct-box">✅ ¡Correcto! Muy bien.</div>', unsafe_allow_html=True)

            # Animación de estrellitas
            st.markdown('<div class="stars">⭐ ✨ 🌟 ✨ ⭐</div>', unsafe_allow_html=True)
            st.balloons()
            time.sleep(1)

        else:
            st.markdown(
                f'<div class="wrong-box">❌ Incorrecto. La respuesta correcta era: {pregunta_data["respuesta"]}</div>',
                unsafe_allow_html=True
            )

    if st.session_state.respondido:
        if st.button("Siguiente pregunta"):
            st.session_state.pregunta_actual += 1
            st.session_state.respondido = False

            if st.session_state.pregunta_actual < len(preguntas):
                nuevas_opciones = preguntas[st.session_state.pregunta_actual]["opciones"]
                st.session_state.opciones_mezcladas = random.sample(
                    nuevas_opciones,
                    len(nuevas_opciones)
                )

            st.rerun()

else:
    st.progress(1.0)
    st.markdown("## 🎉 Trivia finalizada")
    st.write(f"Tu puntaje final fue: **{st.session_state.puntaje} de {len(preguntas)}**")

    if st.session_state.puntaje == 5:
        st.success("🌟 ¡Excelente! Dominas el verbo To Be.")
        st.markdown('<div class="stars">⭐ ✨ 🌟 ✨ ⭐</div>', unsafe_allow_html=True)
        st.balloons()
    elif st.session_state.puntaje >= 3:
        st.info("✨ Muy bien. Solo necesitas practicar un poco más.")
    else:
        st.warning("📚 Sigue practicando el verbo To Be.")

    if st.button("Reiniciar trivia"):
        st.session_state.pregunta_actual = 0
        st.session_state.puntaje = 0
        st.session_state.respondido = False
        st.session_state.opciones_mezcladas = random.sample(
            preguntas[0]["opciones"],
            len(preguntas[0]["opciones"])
        )
        st.rerun()
