import streamlit as st

st.set_page_config(page_title="Cálculo de Ligas Metálicas", page_icon="⚙️", layout="centered")

st.title("⚙️ Cálculo de Ligas Metálicas")

st.markdown("Preencha os dados abaixo para calcular a quantidade de ligas metálicas necessárias.")

# Entradas
peso = st.number_input("Peso do aço (em toneladas):", min_value=0.0, step=0.1, format="%.2f")
p_carbono = st.number_input("Ponto desejado de Carbono:", min_value=0.0, step=0.01, format="%.2f")
p_manganes = st.number_input("Ponto desejado de Manganês:", min_value=0.0, step=0.01, format="%.2f")
p_silicio = st.number_input("Ponto desejado de Silício:", min_value=0.0, step=0.01, format="%.2f")

if st.button("Calcular"):
    if peso == 0:
        st.error("⚠️ O peso do aço deve ser maior que zero.")
    else:
        # Rendimentos
        rendimento_carbono = 95
        rendimento_manganes = 65
        rendimento_silicio = 80

        # Cálculos
        qtd_carbono = (p_carbono * peso * 1000) / rendimento_carbono
        qtd_manganes = (p_manganes * peso * 1000) / rendimento_manganes
        qtd_silicio = (p_silicio * peso * 1000) / rendimento_silicio

        # Resultados
        st.subheader("🔍 Resultado:")
        st.success(f"🔹 Quantidade de **CARBONO**: {qtd_carbono:.2f} kg")
        st.success(f"🔹 Quantidade de **MANGANÊS**: {qtd_manganes:.2f} kg")
        st.success(f"🔹 Quantidade de **SILÍCIO**: {qtd_silicio:.2f} kg")

st.markdown("---")
st.caption("Desenvolvido por Guilherme • Funciona no iOS, Android e PC via navegador 🌎")
