import streamlit as st

st.set_page_config(
    page_title="Cálculo de Ligas Metálicas",
    page_icon="⚙️",
    layout="centered"
)

st.title("⚙️ Cálculo de Ligas Metálicas")
st.subheader("💡 Calcule rapidamente a quantidade ideal de Carbono, Manganês e Silício.")

st.markdown("---")

st.header("📥 Dados de Entrada")

col1, col2 = st.columns(2)

with col1:
    peso = st.number_input("🔧 Peso do aço (toneladas):", min_value=0.0, step=0.1, format="%.2f")
    p_carbono = st.number_input("🌑 Ponto de Carbono:", min_value=0.0, step=0.01, format="%.2f")

with col2:
    p_manganes = st.number_input("🔵 Ponto de Manganês:", min_value=0.0, step=0.01, format="%.2f")
    p_silicio = st.number_input("🟠 Ponto de Silício:", min_value=0.0, step=0.01, format="%.2f")

st.markdown("---")

if st.button("🚀 Calcular"):
    if peso == 0:
        st.error("⚠️ O peso do aço deve ser maior que zero.")
    else:
        rendimento_carbono = 95
        rendimento_manganes = 65
        rendimento_silicio = 75

        qtd_carbono = (p_carbono * peso * 1000) / rendimento_carbono
        qtd_manganes = (p_manganes * peso * 1000) / rendimento_manganes
        qtd_silicio = (p_silicio * peso * 1000) / rendimento_silicio

        st.success("✅ Cálculo realizado com sucesso!")

        with st.expander("🔍 Ver Resultado"):
            st.subheader("📊 Resultado")
            st.success(f"🌑 Carbono: {qtd_carbono:.2f} kg")
            st.success(f"🔵 Manganês: {qtd_manganes:.2f} kg")
            st.success(f"🟠 Silício: {qtd_silicio:.2f} kg")

st.markdown("---")

with st.expander("ℹ️ Como funciona este cálculo?"):
    st.write("""
    O cálculo considera os pontos desejados de cada elemento, 
    multiplica pelo peso do aço (em toneladas) e divide pela eficiência da liga.

    - Carbono: 95%
    - Manganês: 65%
    - Silício: 75%

    Fórmula:
    (ponto desejado * peso do aço * 1000) / rendimento
    """)

st.markdown("---")
st.caption("Desenvolvido por Guilherme Oliveira • 🌐 Funciona no iOS, Android e PC • 🚀 Powered by Streamlit")
