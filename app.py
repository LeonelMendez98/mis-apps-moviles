import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página para móviles
st.set_page_config(page_title="Mi App de Bolsillo", layout="centered")

st.title("🚀 Mi Primera App")
st.write("Esta app corre desde la nube pero la veo en mi celular.")

# Sección de entrada de datos
st.subheader("Calculadora Rápida")
num1 = st.number_input("Ingresa un valor A", value=10)
num2 = st.slider("Selecciona valor B", 0, 100, 50)

resultado = num1 * num2
st.success(f"El resultado de A x B es: {resultado}")

# Sección de visualización
st.subheader("Gráfico de Prueba")
datos = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Crecimiento', 'Volatilidad']
)
st.line_chart(datos)

if st.button("Saludar"):
    st.balloons()
    st.write("¡Funciona perfecto!")
