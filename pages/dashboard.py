import plotly.express as px
import streamlit as st

# def render():
#     st.title("Dashboard Principal")
#     data = {
#         "Fecha": ["2023-12-01", "2023-12-02", "2023-12-03"],
#         "Tasa de Defectos": [5, 3, 4]
#     }
#     df = pd.DataFrame(data)
#     fig = px.bar(df, x="Fecha", y="Tasa de Defectos", title="Tasa de Defectos")
#     st.plotly_chart(fig)


# pages/dashboard.py
import streamlit as st

def render():
    if not st.session_state.logged_in:
        st.error("Debes iniciar sesión para acceder al Dashboard.")
        return

    st.title("Dashboard")
    st.write("Bienvenido al panel principal. Aquí encontrarás tus herramientas y métricas clave.")
