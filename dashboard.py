import requests
import streamlit as st

# Configuração da página do painel
st.set_page_config(
    page_title="Dashboard - Estação Meteorológica PD-II",
    page_icon="⛅",
    layout="wide",
)

st.title("⛅ Painéis do Cidadão - Estação Meteorológica Inteligente")
st.markdown(
    "Monitoramento em tempo real das condições meteorológicas, qualidade do"
    " ar e alertas para a comunidade."
)

# URL do endpoint da API Flask criado na Etapa 4
API_URL = "http://m4rcos0013.pythonanywhere.com/api/historico"


# Função para carregar os dados da API
def carregar_dados_api():
  try:
    resposta = requests.get(API_URL)
    if resposta.status_code == 200:
      return resposta.json()
  except Exception as e:
    st.error(
        f"Não foi possível ligar ao servidor da API em {API_URL}. Erro: {e}"
    )
  return []

