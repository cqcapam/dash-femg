import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
from scipy.stats import spearmanr

# Use the full page instead of a narrow central column


# Title
st.title("Análises Inferenciais")

#Spearman 
st.subheader("Coeficiente de Spearman")

# Data
df = pd.read_parquet('datas/newdf.parquet')

# selection for location
all_locations = df['local'].unique()
selected_locations = st.selectbox('Selecione o ponto:', all_locations)

filtered_df = df[df['local'] == selected_locations]

# Graphs
cor = ['#7DCEA0']
p_mang = px.scatter(filtered_df, x='ferro', y='mang', title=f"Dispersão: {selected_locations}", template="simple_white", trendline="ols",color_discrete_sequence=cor,
                 labels={'ferro': 'Ferro',
                         'mang': 'Manganês'})

# Table results by point

# Função para interpretar o valor de p
def interpretar_p_valor(p_valor):
    if p_valor < 0.05:
        return '🟢 Significativo'
    else:
        return '🔴 Não Significativo'

# Função para interpretar o coeficiente de correlação
def interpretar_coeficiente(coeficiente):
    if abs(coeficiente) >= 0.5:
        return '🟢 Forte'
    elif abs(coeficiente) >= 0.3:
        return '🟡 Moderado'
    else:
        return '🔴 Fraco'

# Spearman 
grouped = df.groupby('local')
resultados = []

for name, group in grouped:
    coeficiente_spearman, p_valor = spearmanr(group['ferro'], group['mang'])
    resultados.append([
        name, 
        coeficiente_spearman, 
        round(p_valor, 3), 
        interpretar_p_valor(p_valor), 
        interpretar_coeficiente(coeficiente_spearman)
    ])

# Criar um DataFrame com os resultados
resultados_df = pd.DataFrame(resultados, columns=['Ponto', 'Coeficiente', 'Valor de p', 'Análise valor de p', 'Análise Coeficiente'])

# Columns
# Space out the maps so the first one is 2x the size of the other three
c1, c2, c3 = st.columns((3, 1, 3))

# Contents column 1
c1.plotly_chart(p_mang, theme='streamlit', use_column_width=True)

# Contents column 2
c3.write(resultados_df.to_html(index=False), unsafe_allow_html=True)

st.divider()