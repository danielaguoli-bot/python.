
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Instrumentos Musicales",
    page_icon="🎵",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #f8f7ff;
    color: #29263d;
}

h1 {
    color: #401472;
}

h2 {
    color: #7957d5;
}

h3 {
    color: #7957d5;
}

.tarjeta {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.icono {
    font-size: 60px;
}

.titulo-portada {
    font-size: 45px;
    font-weight: bold;
    color: #29263d;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="titulo-portada">🎵 Instrumentos Musicales</div>',
    unsafe_allow_html=True
)

st.write(
    "Bienvenido a nuestra página sobre instrumentos musicales. "
    "Aquí podrás conocer diferentes instrumentos, sus familias "
    "y algunas de sus características."
)


opcion = st.selectbox(
    "Selecciona una sección:",
    [
        "Inicio",
        "Cuerda",
        "Viento",
        "Percusión",
        "Teclado",
        "Tabla de instrumentos",
        "Gráfico"
    ]
)


if opcion == "Inicio":

    st.header("🎶 Conoce el mundo de la música")

    st.write(
        "Los instrumentos musicales son objetos creados para producir "
        "sonidos y formar parte de diferentes expresiones musicales."
    )

    st.subheader("🎼 Familias de instrumentos")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎸</div>
        <h3>Cuerda</h3>
        <p>Producen sonido mediante la vibración de sus cuerdas.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎺</div>
        <h3>Viento</h3>
        <p>Producen sonido mediante la vibración del aire.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🥁</div>
        <h3>Percusión</h3>
        <p>Producen sonido al ser golpeados, sacudidos o frotados.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎹</div>
        <h3>Teclado</h3>
        <p>Utilizan teclas para producir diferentes sonidos.</p>
        </div>
        """, unsafe_allow_html=True)


elif opcion == "Cuerda":

    st.header("🎸 Instrumentos de cuerda")

    st.write(
        "Los instrumentos de cuerda producen sonido mediante "
        "la vibración de sus cuerdas."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎸</div>
        <h3>Guitarra</h3>
        <p>Instrumento de cuerda utilizado en muchos géneros musicales.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎻</div>
        <h3>Violín</h3>
        <p>Instrumento de cuerda conocido por su sonido expresivo.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎼</div>
        <h3>Arpa</h3>
        <p>Instrumento de cuerda formado por numerosas cuerdas.</p>
        </div>
        """, unsafe_allow_html=True)


elif opcion == "Viento":

    st.header("🎺 Instrumentos de viento")

    st.write(
        "Los instrumentos de viento producen sonido mediante "
        "la vibración del aire."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎺</div>
        <h3>Trompeta</h3>
        <p>Instrumento de viento utilizado en diferentes estilos musicales.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎷</div>
        <h3>Saxofón</h3>
        <p>Instrumento de viento utilizado especialmente en jazz.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🪈</div>
        <h3>Flauta</h3>
        <p>Instrumento de viento que produce sonido mediante el aire.</p>
        </div>
        """, unsafe_allow_html=True)


elif opcion == "Percusión":

    st.header("🥁 Instrumentos de percusión")

    st.write(
        "Los instrumentos de percusión producen sonido principalmente "
        "cuando son golpeados, sacudidos o frotados."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🥁</div>
        <h3>Batería</h3>
        <p>Conjunto de instrumentos de percusión.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🪘</div>
        <h3>Tambor</h3>
        <p>Instrumento que produce sonido al ser golpeado.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎵</div>
        <h3>Maracas</h3>
        <p>Instrumentos que producen sonido al ser sacudidos.</p>
        </div>
        """, unsafe_allow_html=True)


elif opcion == "Teclado":

    st.header("🎹 Instrumentos de teclado")

    st.write(
        "Los instrumentos de teclado utilizan teclas para producir "
        "diferentes sonidos."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎹</div>
        <h3>Piano</h3>
        <p>Instrumento de teclado utilizado en numerosos géneros.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎹</div>
        <h3>Órgano</h3>
        <p>Instrumento de teclado que produce diferentes sonidos.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎹</div>
        <h3>Teclado electrónico</h3>
        <p>Instrumento electrónico capaz de producir diferentes sonidos.</p>
        </div>
        """, unsafe_allow_html=True)


elif opcion == "Tabla de instrumentos":

    st.header("📋 Tabla de instrumentos")

    datos = {
        "Instrumento": [
            "Guitarra", "Violín", "Arpa",
            "Trompeta", "Saxofón", "Flauta",
            "Batería", "Tambor", "Maracas",
            "Piano", "Órgano", "Teclado electrónico"
        ],

        "Familia": [
            "Cuerda", "Cuerda", "Cuerda",
            "Viento", "Viento", "Viento",
            "Percusión", "Percusión", "Percusión",
            "Teclado", "Teclado", "Teclado"
        ]
    }

    tabla = pd.DataFrame(datos)

    st.dataframe(
        tabla,
        use_container_width=True
    )


elif opcion == "Gráfico":

    st.header("📊 Instrumentos por familia")

    datos_grafico = {
        "Familia": [
            "Cuerda",
            "Viento",
            "Percusión",
            "Teclado"
        ],

        "Cantidad": [
            3,
            3,
            3,
            3
        ]
    }

    grafico = pd.DataFrame(datos_grafico)

    st.bar_chart(
        grafico.set_index("Familia")
    )


st.markdown("---")

st.write(
    "🎵 Mundo Musical | Proyecto desarrollado con Python y Streamlit"
)


