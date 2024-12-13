# pages/login.py
import streamlit as st
from services.auth import authenticate

def render():
    st.title("Inicio de Sesión")
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar Sesión"):
        if authenticate(email, password):
            st.success("Inicio de sesión exitoso. Redirigiendo al Dashboard...")
            # Cambiamos experimental_set_query_params por query_params
            st.query_params.update({"page": "Dashboard"})
        else:
            st.error("Usuario no registrado o credenciales incorrectas. Por favor, regístrate.")
