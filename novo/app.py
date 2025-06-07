import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar o CSV com tratamento de erros
@st.cache_data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', delimiter=",")  # Ignora linhas problemáticas
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo CSV: {e}")
        return None

# Carregar dados
file_path = "MS_Financial Sample.csv"
df = load_data(file_path)

# Título do app
st.title("📊 Dashboard Interativo com Streamlit")

if df is not None:
    # Exibir informações do dataset
    st.write("### Visualização dos dados:")
    st.dataframe(df.head())

    # Mostrar informações gerais
    st.write("### Informações do Dataset:")
    st.write(df.describe())  # Estatísticas gerais das colunas numéricas

    # Exemplo de gráfico de barras
    colunas_numericas = df.select_dtypes(include=["number"]).columns
    if len(colunas_numericas) >= 1:
        coluna_grafico = st.selectbox("Escolha uma coluna para o gráfico de barras:", colunas_numericas)
        st.write(f"Gráfico de barras para {coluna_grafico}:")
        st.bar_chart(df[coluna_grafico])

    # Exemplo de gráfico de dispersão
    st.write("### Gráfico de dispersão:")
    if len(colunas_numericas) >= 2:
        col_x = st.selectbox("Escolha a coluna X:", colunas_numericas)
        col_y = st.selectbox("Escolha a coluna Y:", colunas_numericas)

        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=col_x, y=col_y, ax=ax)
        st.pyplot(fig)
else:
    st.error("Não foi possível carregar os dados. Verifique o arquivo CSV.")

