# App_con_ChatGPT


# Importar la biblioteca Streamlit
import streamlit as st

# Título de la aplicación
st.title("Mi primera app")

# Autor
st.subheader("Autor: Esta app fue elaborada por Juan Camilo López Morales")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Verificar si se ingresó un nombre
if nombre_usuario:
    # Mostrar mensaje de bienvenida
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
