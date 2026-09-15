import pandas as pd
import streamlit as st

# Configuração da página para ficar amigável no celular
st.set_page_config(page_title="Calculadora Steck", page_icon="🔍")
st.title("🔍 Buscador de Preços Steck")

@st.cache_data
def carregar_dados():
    # Carrega exatamente o arquivo que você mencionou
    df = pd.read_csv("tabela_de_preços_steck.csv")
    return df

try:
    tabela = carregar_dados()
    
    # Caixa de pesquisa
    busca = st.text_input("Digite o código ou nome do produto (ex: SDD61C32):")

    if busca:
        # Filtra a tabela procurando o texto digitado em qualquer coluna
        filtro = tabela.astype(str).apply(lambda row: row.str.contains(busca, case=False).any(), axis=1)
        resultado = tabela[filtro]

        if not resultado.empty:
            st.success(f"{len(resultado)} item(ns) encontrado(s)!")
            st.dataframe(resultado, use_container_width=True)
        else:
            st.warning("Nenhum produto encontrado com esse código.")

except FileNotFoundError:
    st.error("Erro: O arquivo 'tabela_de_preços_steck.csv' não foi encontrado. Verifique se ele está na mesma pasta.")