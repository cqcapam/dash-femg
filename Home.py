import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Dashboard - Ferro e Manganês",
    page_icon=":droplet:",
    layout="wide"
)

# Estilo do cabeçalho
st.markdown("""
    <h1 style='font-size: 42px; color: #004d7b; margin-bottom: 0;'>💧 Análises de Ferro e Manganês</h1>
    <p style='font-size: 18px; color: #333;'>Análise de Ferro e Manganês | Construído com Python + Streamlit</p>
""", unsafe_allow_html=True)

st.divider()

# Mensagem explicativa
st.markdown("""
### 📊 O que você vai encontrar neste painel?

Explore os dados de monitoramento de qualidade da água em diferentes pontos e anos, visualizando:

- Séries históricas de **Ferro** e **Manganês**
- Comparações por ponto e por ano
- Indicadores de conformidade nos gráficos
- Análises estatísticas (coeficiente de Spearman)

Use o menu lateral para navegar entre as seções.

---

### 🔁 Atualização de dados

Para atualizar os dados do dashboard, basta substituir o arquivo:
datas/newdf.parquet disponível no repositório do github.

Certifique-se de manter o mesmo formato de colunas e nomes!

---
""")


