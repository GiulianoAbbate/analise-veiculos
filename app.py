import streamlit as st
import pandas as pd
import plotly.express as px

# Configurando o título da página
st.header('Análise de Vendas de Carros')

# Lendo o conjunto de dados
# O caminho foi ajustado para apontar para a pasta 'notebooks'
car_data = pd.read_csv('notebooks/vehicles.csv')

# Criando uma caixa de seleção para o histograma
build_histogram = st.checkbox('Criar um histograma de quilometragem')

if build_histogram: # se a caixa de seleção for marcada
    st.write('Criando um histograma para a distribuição de quilometragem')
    
    # Criar um histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Criando uma caixa de seleção para o gráfico de dispersão
build_scatter = st.checkbox('Criar um gráfico de dispersão de Preço vs. Quilometragem')

if build_scatter: # se a caixa de seleção for marcada
    st.write('Criando um gráfico de dispersão para Preço vs. Quilometragem')
    
    # Criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)