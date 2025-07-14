import streamlit as st
st.title("Teste de Funcionamento")

# Teste Plotly (modo seguro)
try:
    import plotly.express as px
    st.success("✅ Plotly instalado corretamente!")
    df = px.data.iris()
    st.plotly_chart(px.scatter(df, x="sepal_width", y="sepal_length"))
except Exception as e:
    st.error(f"❌ Falha no Plotly: {str(e)}")
    st.info("Isso indica um problema no ambiente do Streamlit Cloud")

# Teste de arquivos
try:
    with open("inteligencia_contratual_limpa.csv") as f:
        st.success("✅ Arquivo CSV encontrado!")
except:
    st.warning("⚠️ Arquivo CSV não encontrado")
