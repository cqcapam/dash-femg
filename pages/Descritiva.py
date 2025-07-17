
import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from streamlit_extras.metric_cards import style_metric_cards


# Title
st.title("Análise descritiva")

# Data
df = pd.read_parquet('datas/newdf.parquet')


#line 1 
c1, c2, c3,= st.columns((3,0.5,3))

# selection for location
with c1:
        anos = df['ano'].unique()
        ano_selecionado = st.selectbox('Selecione o Ano', anos)
        df_ano = df[df['ano'] == ano_selecionado]
        

# Select a year 
with c3:
        all_locations = df['local'].unique()
        selected_locations = st.selectbox('Selecione o ponto:', all_locations)
        filtered_df = df[df['local'] == selected_locations]


# Graphs
p_mang = px.line(filtered_df, x='data', y='mang', title='Valores de Manganês', color='local', template="simple_white",
                 labels={'data': 'Anos',
                         'mang': 'Manganês',
                         'local': 'Pontos'})
p_mang.add_shape(
    type="line",
    x0=filtered_df['data'].min(), x1=filtered_df['data'].max(),
    y0=0.100, y1=0.100,
    line=dict(color="Red", width=3.5, dash="dash"),
)

p_fe = px.line(filtered_df, x='data', y='ferro', title='Valores de Ferro', color='local', template="simple_white",
               labels={'data': 'Anos',
                       'ferro': 'Ferro',
                       'local': 'Pontos'})

p_fe = go.Figure(p_fe)

p_fe.add_shape(
    type="line",
    x0=filtered_df['data'].min(), x1=filtered_df['data'].max(),
    y0=0.30, y1=0.30,
    line=dict(color="Red", width=3.5, dash="dash"),
)

#others views

#analysis by year
by_year = df['ano'].value_counts().reset_index()
by_year.columns = ['ano', 'count']
by_year['ano'] = by_year['ano'].astype(str)

#graph of analisys by year
cores = ['#C0392B','#9B59B6','#3498DB','#16A085','#F39C12',"rgba(211, 84, 0, 0.63)",'#4B6888']

p_year = px.bar(by_year, x='ano', y='count', color='ano', color_discrete_sequence=cores, title='Análises por ano', template="simple_white",
                 labels={'ano':'Ano',
                         'count':'Num de análises'}, 
                 category_orders={'ano':['2018','2019','2020','2021','2022','2023','2024']})

#metric cards analysis out of limit 
cores = ["#FA0213"]
#num fe out
num_analises_fe = len(df_ano)
num_desconformes_fe = len(df_ano[df_ano['ferro'] > 0.3])

#num mang out
num_analises_mn = len(df_ano)
num_desconformes_mn = len(df_ano[df_ano['mang'] > 0.1])

#num ferro out por ponto 
num_analises_fe_ponto = len(filtered_df)
num_desconformes_fe_ponto = len(filtered_df[filtered_df['ferro'] > 0.3])

#num mang out por ponto 
num_analises_mn_ponto = len(filtered_df)
num_desconformes_mn_ponto = len(filtered_df[filtered_df['mang'] > 0.1])

#desconformes ferro e mang
desconformes_fe_mn = df[(df['ferro'] > 0.3) & (df['mang'] > 0.1)]
ocorrencias_fe_mn = desconformes_fe_mn['local'].value_counts().reset_index()
ocorrencias_fe_mn.columns = ['Ponto', 'Ocorrências']

#média de análises por ano 
analises_por_ano = df.groupby('ano').size()
media_por_ano = analises_por_ano.mean()
media_por_ano_int = int(round(media_por_ano)) # type: ignore
#metrics
c1,c2,c3,c4,c5,c6 = st.columns((2,2,2,2,2,0.5))

#column 1 - ferro
c1.metric(label=f"Análises de Ferro: {ano_selecionado}", value=num_analises_fe, delta=f" Desconformes: {num_desconformes_fe}", delta_color="inverse")

#column 2 - mang 
c2.metric(label=f"Análises de Manganês: {ano_selecionado}", value=num_analises_mn, delta=f"Desconformes: {num_desconformes_mn}", delta_color="inverse")

#column 3 - média de analise por ano 
c3.metric(label="Média de análises por ano:", value=media_por_ano_int)

#column 4 - ferro by local
c4.metric(label=f"Análises de Ferro: {selected_locations}",value=num_analises_fe_ponto, delta=f"Desconformes: {num_desconformes_fe_ponto}", delta_color='inverse')

#column 5 - mang by local
c5.metric(label=f"Análises de Manganês: {selected_locations}", value=num_analises_mn_ponto, delta=f"Desconformes:{num_desconformes_mn_ponto}", delta_color='inverse')


# Columns
# Space out the maps so the first one is 2x the size of the other three
c1, c2, c3, c4, c5 = st.columns((3,0.5,3,3,2))

# Contents column 1
c1.plotly_chart(p_year, theme='streamlit', use_container_width=True)

# Contents column 3
c3.plotly_chart(p_fe, theme='streamlit', use_column_width=True)

#content column 4
c4.plotly_chart(p_mang, theme='streamlit', use_column_width=True)

with c5:
        st.write("")
        with st.expander("Desconformidades frequentes"):                
                st.write(ocorrencias_fe_mn.to_html(index=False), unsafe_allow_html=True)