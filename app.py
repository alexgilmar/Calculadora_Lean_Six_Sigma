# app.py
import streamlit as st
from pages import login, dashboard, registro, acerca

# Páginas disponibles
PAGES = {
    "Login": login,
    "Acerca de": acerca,
    "Dashboard": dashboard,
}

# Función principal
def main():
    # Inicializamos el estado de sesión
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False  # Por defecto, el usuario no está logueado

    # Configuración del menú dinámico
    if st.session_state.logged_in:
        menu = ["Dashboard", "Acerca de"]
    else:
        menu = ["Login", "Acerca de"]

    # Mostrar el menú
    page = st.sidebar.selectbox("app", menu)

    # Renderizar la página seleccionada
    if page == "Dashboard" and not st.session_state.logged_in:
        st.error("Debes iniciar sesión para acceder al Dashboard.")
    else:
        PAGES[page].render()

if __name__ == "__main__":
    main()


# # app.py (modificado)
# def main():

    
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False

#     if st.session_state.logged_in:
#         menu = ["Dashboard", "Acerca de", "Cerrar Sesión"]
#     else:
#         menu = ["Login", "Acerca de"]

#     page = st.sidebar.selectbox("app", menu)

#     if page == "Cerrar Sesión":
#         st.session_state.logged_in = False
#         st.experimental_rerun()

#     elif page == "Dashboard" and not st.session_state.logged_in:
#         st.error("Debes iniciar sesión para acceder al Dashboard.")
#     else:
#         PAGES[page].render()
