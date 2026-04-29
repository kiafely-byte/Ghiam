import streamlit as st
import random
import time

# =============================
# CONFIGURACIÓN DE LA PÁGINA
# =============================
st.set_page_config(
    page_title="Trivia Villanas Disney",
    page_icon="🖤",
    layout="centered"
)

# =============================
# ESTILOS VISUALES
# =============================
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #7B1FA2;
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
        border-left: 6px solid #4CAF50;
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
</style>
""", unsafe_allow_html=True)

# =============================
# BANCO DE PREGUNTAS
# =============================
preguntas = [
    {
        "pregunta": "¿Qué villana quería robar la voz de Ariel?",
        "opciones": ["Úrsula", "Maléfica", "Cruella de Vil", "Madre Gothel"],
        "respuesta": "Úrsula"
    },
    {
        "pregunta": "¿Qué villana lanzó una maldición sobre la princesa Aurora?",
        "opciones": ["Maléfica", "Reina Grimhilde", "Lady Tremaine", "Yzma"],
        "respuesta": "Maléfica"
    },
    {
        "pregunta": "¿Qué villana quería hacerse un abrigo con cachorros dálmatas?",
        "opciones": ["Cruella de Vil", "Úrsula", "Madre Gothel", "Reina de Corazones"],
        "respuesta": "Cruella de Vil"
    },
    {
        "pregunta": "¿Qué villana mantenía encerrada a Rapunzel para usar el poder de su cabello?",
        "opciones": ["Madre Gothel", "Maléfica", "Yzma", "Lady Tremaine"],
        "respuesta": "Madre Gothel"
    },
    {
        "pregunta": "¿Qué villana de Blancanieves usa una manzana envenenada?",
        "opciones": ["Reina Grimhilde", "Úrsula", "Cruella de Vil", "Madre Gothel"],
        "respuesta": "Reina Grimhilde"
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
st.markdown('<div class="main-title">🖤 Trivia de Villanas Disney</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Responde 5 preguntas y descubre cuánto sabes sobre las villanas más icónicas.</div>', unsafe_allow_html=True)

# =============================
# MOSTRAR PREGUNTA
# =============================
if st.session_state.pregunta_actual < len(preguntas):
    pregunta_data = preguntas[st.session_state.pregunta_actual]

    st.progress((st.session_state.pregunta_actual) / len(preguntas))
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
            st.markdown('<div class="correct-box">✅ ¡Correcto! La villana no pudo engañarte.</div>', unsafe_allow_html=True)

            # Animación cuando acierta
            st.balloons()
            time.sleep(1)
            st.snow()

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
        st.success("👑 ¡Perfecto! Eres una experta en villanas Disney.")
        st.balloons()
    elif st.session_state.puntaje >= 3:
        st.info("✨ Muy bien, conoces bastante sobre las villanas.")
    else:
        st.warning("🖤 Puedes mejorar, pero las villanas aún tienen secretos para ti.")

    if st.button("Reiniciar trivia"):
        st.session_state.pregunta_actual = 0
        st.session_state.puntaje = 0
        st.session_state.respondido = False
        st.session_state.opciones_mezcladas = random.sample(
            preguntas[0]["opciones"],
            len(preguntas[0]["opciones"])
        )
        st.rerun()
