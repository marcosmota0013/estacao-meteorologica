import requests
import streamlit as st

# Configuração da página do painel
st.set_page_config(
    page_title="Dashboard - Estação Meteorológica PD-II",
    page_icon="⛅",
    layout="wide",
)

st.title("⛅ Previão do Tempo - MiniEstação Meteorológica Inteligente")
st.markdown(
    "Monitoramento em tempo real das condições meteorológicas, qualidade do"
    " ar e alertas para a comunidade."
)

# URL do endpoint da API Flask 
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


# Obter dados
dados = carregar_dados_api()

if not dados:
  st.warning(
      "Aviso: O servidor está ativo, mas ainda não existem registos de"
      " telemetria."
  )
else:
  # Pegar no registo mais recente (último elemento da lista)
  ultimo = dados[-1]

  #  SECÇÃO 1: CARTÕES DE INDICADORES (KPIs) 
  st.markdown("### 📊 Condições Atuais")
  col1, col2, col3, col4 = st.columns(4)

  with col1:
    st.metric(label="Temperatura", value=f"{ultimo.get('temp', 0):.1f} °C")
  with col2:
    st.metric(label="Humidade do Ar", value=f"{ultimo.get('humidity', 0):.1f} %")
  with col3:
    st.metric(
        label="Pressão Atmosférica",
        value=f"{ultimo.get('pressure', 0):.1f} hPa",
    )
  with col4:
    alerta_s1 = ultimo.get("alert", 0)
    estado_txt = "⚠️ ALERTA ATIVO" if alerta_s1 == 1 else "✅ NORMAL (Seguro)"
    st.metric(label="Estado de Alerta (S1)", value=estado_txt)

  st.markdown("---")

  # SECÇÃO 2: DETALHES E GEOLOCALIZAÇÃO 
  col_esq, col_dir = st.columns([2, 1])

  with col_esq:
    st.subheader("📈 Últimos Registos Recebidos")
    st.json(dados[-5:])

  with col_dir:
    st.subheader("📍 Geolocalização da Estação")
    st.info(
        "**Coordenadas do Posto PD-II:**\n- Latitude: -16.82\n- Longitude:"
        " -49.25"
    )
    st.caption("Localização fixa monitorizada.")

  # SECÇÃO 3: HISTÓRICO COMPLETO 
  with st.expander("🔍 Ver Todos os Dados em JSON Bruto"):
    st.write(dados)
