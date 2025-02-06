import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="TSS Trouble Shooting Services",
    page_icon="🚀",
    layout="wide"
)

# Título y descripción de la empresa
st.title("🚀 Trouble Shooting Services")
st.markdown("""
**TSS Trouble Shooting Services** es una empresa líder en tecnología innovadora que ofrece soluciones personalizadas 
para mejorar la eficiencia y competitividad de tu negocio. Desde desarrollo de software hasta inteligencia 
artificial, estamos comprometidos con el éxito de nuestros clientes.
""")

# Sección de servicios
st.header("💡 Nuestros Servicios")
services = {
    "Desarrollo de Software": "Creación de aplicaciones web y móviles a medida.",
    "Inteligencia Artificial": "Soluciones avanzadas de IA para optimización de procesos.",
    "Ciberseguridad": "Protección integral para tus sistemas y datos.",
    "Consultoría Tecnológica": "Asesoramiento estratégico para transformación digital."
}

for service, description in services.items():
    st.subheader(service)
    st.write(description)

# Gráfico interactivo
st.header("📊 Rendimiento de nuestras soluciones")
st.markdown("""
A continuación, se muestra un gráfico interactivo que refleja el impacto de nuestras soluciones en diferentes sectores.
""")

# Datos ficticios para el gráfico
data = pd.DataFrame({
    "Sector": ["Financiero", "Salud", "Educación", "Retail", "Manufactura"],
    "Mejora (%)": [25, 30, 20, 35, 40]
})

fig = px.bar(data, x="Sector", y="Mejora (%)", title="Impacto por Sector", color="Mejora (%)", 
             labels={"Mejora (%)": "Incremento en Eficiencia (%)"}, template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

# Formulario de contacto
st.header("📧 Contáctanos")
st.markdown("""
¿Quieres saber más sobre cómo podemos ayudarte? Completa el siguiente formulario y nos pondremos en contacto contigo.
""")

with st.form("contact_form"):
    name = st.text_input("Nombre")
    email = st.text_input("Correo Electrónico")
    message = st.text_area("Mensaje")
    submit = st.form_submit_button("Enviar")

    if submit:
        if name and email and message:
            st.success(f"Gracias por contactarnos, {name}. ¡Nos pondremos en contacto pronto!")
        else:
            st.error("Por favor, completa todos los campos.")

# Footer
st.markdown("---")
st.markdown("""
© 2023 Trouble Shooting Services. Todos los derechos reservados.
""")
