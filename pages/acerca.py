# pages/acerca.py
import streamlit as st

def render():
    st.title("Acerca de esta aplicación")
    st.markdown("""
    ## Bienvenido a nuestra aplicación
    Esta plataforma está diseñada para ofrecer herramientas avanzadas de análisis y gestión. A continuación, te explicamos sus principales características:

    ### Herramientas disponibles:
    - **Dashboard**: Un panel interactivo para visualizar datos y métricas clave.
    - **Herramientas LSS**: Funcionalidades específicas para Lean Six Sigma, como análisis de procesos y cálculos estadísticos.
    - **Registro de usuarios**: Un sistema para gestionar el acceso de usuarios de manera segura.

    ### Propósito
    Esta aplicación está diseñada para ayudar a profesionales y empresas a optimizar sus procesos y tomar decisiones basadas en datos.

    Si tienes preguntas o comentarios, no dudes en contactarnos.
    """)
