import streamlit as st

st.set_page_config(
    page_title="Cálculo de Ligas Metálicas",
    page_icon="⚙️",
    layout="centered"
)

st.title("⚙️ Cálculo de Ligas Metálicas")
st.subheader("💡 Informe os dados e clique em calcular.")

st.markdown("---")

st.header("📥 Dados de Entrada")

# 🔢 Entradas com valores exemplares
peso = st.number_input("🔧 Peso do aço (toneladas):", min_value=0.0, step=0.1, value=0.0, placeholder="Ex: 50")

p_carbono = st.number_input("🌑 Ponto de Carbono:", min_value=0.0, step=0.01, value=0.0, placeholder="Ex: 0.50")

p_manganes = st.number_input("🔵 Ponto de Manganês:", min_value=0.0, step=0.01, value=0.0, placeholder="Ex: 1.20")

p_silicio = st.number_input("🟠 Ponto de Silício:", min_value=0.0, step=0.01, value=0.0, placeholder="Ex: 0.80")

st.markdown("---")

# 🔥 Botão de cálculo
if st.button("🚀 Calcular"):
    if peso <= 0:
        st.error("⚠️ O peso do aço deve ser maior que zero.")
    else:
        rendimento_carbono = 95
        rendimento_manganes = 65
        rendimento_silicio = 75

        qtd_carbono = (p_carbono * peso * 1000) / rendimento_carbono
        qtd_manganes = (p_manganes * peso * 1000) / rendimento_manganes
        qtd_silicio = (p_silicio * peso * 1000) / rendimento_silicio

        st.subheader("📊 Resultado")
        st.success(f"🌑 Carbono: {qtd_carbono:.2f} kg")
        st.success(f"🔵 Manganês: {qtd_manganes:.2f} kg")
        st.success(f"🟠 Silício: {qtd_silicio:.2f} kg")

st.markdown("---")

st.caption("Desenvolvido por Guilherme Oliveira • 🌐 Funciona no iOS, Android e PC • 🚀 Powered by Streamlit")
