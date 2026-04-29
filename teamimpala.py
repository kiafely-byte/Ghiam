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
    .guitar-animation {
        text-align: center;
        font-size: 48px;
        margin-top: 20px;
        animation: guitarMove 0.8s infinite alternate;
    }
    @keyframes guitarMove {
        from { transform: rotate(-8deg) scale(1); opacity: 0.7; }
        to { transform: rotate(8deg) scale(1.25); opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# =============================
# BANCO DE PREGUNTAS
# =============================
preguntas = [
    {
        "pregunta": "¿Quién es el principal creador detrás del proyecto Tame Impala?",
        "opciones": ["Kevin Parker", "Alex Turner", "Julian Casablancas", "Matty Healy"],
        "respuesta": "Kevin Parker"
    },
    {
        "pregunta": "¿Qué canción de Tame Impala incluye la frase 'The less I know the better'?",
        "opciones": ["The Less I Know the Better", "Let It Happen", "Borderline", "Eventually"],
        "respuesta": "The Less I Know the Better"
    },
    {
        "pregunta": "¿A qué álbum pertenece la canción 'Let It Happen'?",
        "opciones": ["Currents", "Lonerism", "The Slow Rush", "Innerspeaker"],
        "respuesta": "Currents"
    },
    {
        "pregunta": "¿Cuál de estas canciones pertenece al álbum 'The Slow Rush'?",
        "opciones": ["Borderline", "Elephant", "Mind Mischief", "Solitude Is Bliss"],
        "respuesta": "Borderline"
    },
    {
        "pregunta": "¿Cuál de estas canciones es de Tame Impala?",
        "opciones": ["Feels Like We Only Go Backwards", "Do I Wanna Know?", "Last Nite", "Somebody Else"],
        "respuesta": "Feels Like We Only Go Backwards"
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
st.markdown('<div class="main-title">🎸 Trivia de Tame Impala 🎸</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Responde 5 preguntas sobre canciones, álbumes y datos de Tame Impala.</div>', unsafe_allow_html=True)

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
            st.markdown('<div class="correct-box">✅ ¡Correcto! Estás en modo psicodélico.</div>', unsafe_allow_html=True)

            # Animación de guitarras al acertar
            st.markdown('<div class="guitar-animation">🎸 🎶 🎸 🎶 🎸</div>', unsafe_allow_html=True)
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
        st.success("🎸 ¡Perfecto! Eres fan total de Tame Impala.")
        st.markdown('<div class="guitar-animation">🎸 🎶 🎸 🎶 🎸</div>', unsafe_allow_html=True)
        st.balloons()
    elif st.session_state.puntaje >= 3:
        st.info("✨ Muy bien. Conoces bastante de Tame Impala.")
    else:
        st.warning("🎧 Sigue escuchando más temas de Tame Impala.")

    if st.button("Reiniciar trivia"):
        st.session_state.pregunta_actual = 0
        st.session_state.puntaje = 0
        st.session_state.respondido = False
        st.session_state.opciones_mezcladas = random.sample(
            preguntas[0]["opciones"],
            len(preguntas[0]["opciones"])
        )
        st.rerun()
