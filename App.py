import streamlit as st
import pandas as pd
import plotly.express as px

# ======================================
# DADOS FICTÍCIOS (SIMULANDO SUA PLANILHA)
# ======================================
data = {
    "ID_Contrato": ["C001", "C002", "C003", "C004", "C005"],
    "Projeto": ["Florestas_Verdes", "PSA_Norte", "Biodiversidade", "Logistica_ESG", "Fundiario_Sul"],
    "Valor_Total_R$": [1500000, 800000, 1200000, 950000, 2000000],
    "Status": ["Em execução", "Finalizado", "Inadimplente", "Rescindido", "Em execução"],
    "ESG_Score": [78, 56, 65, 86, 61],
    "Risco_Contratual": ["Baixo", "Alto", "Médio", "Baixo", "Alto"]
}

df = pd.DataFrame(data)

# ======================================
# CONFIGURAÇÃO DO APP
# ======================================
st.set_page_config(layout="wide", page_title="Análise Contratos", page_icon="📊")
st.title("📊 Dashboard de Contratos (Versão Simplificada)")

# ======================================
# VISUALIZAÇÕES PRINCIPAIS
# ======================================
st.subheader("🔍 Visão Geral")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Contratos", len(df))
col2.metric("Valor Total", f"R$ {df['Valor_Total_R$'].sum():,}")
col3.metric("Média ESG", f"{df['ESG_Score'].mean():.1f}")

# Gráfico 1: Valor por Projeto
st.subheader("💰 Valor por Projeto")
fig = px.bar(df, x="Projeto", y="Valor_Total_R$", color="Status")
st.plotly_chart(fig, use_container_width=True)

# Gráfico 2: Distribuição ESG
st.subheader("🌱 Performance ESG")
fig = px.pie(df, names="Risco_Contratual", values="ESG_Score")
st.plotly_chart(fig, use_container_width=True)

# Tabela Interativa
st.subheader("📋 Dados Completos")
st.dataframe(df, use_container_width=True)

# ======================================
# RODAPÉ
# ======================================
st.markdown("---")
st.caption("Dashboard criado com Streamlit - Dados fictícios para demonstração")
