import streamlit as st
import pickle
import pandas as pd
import plotly.express as px

import data_handler
from data_analysis import data_analysis

st.title('Trabalho GB - Streamlit')

data = data_handler.load_data()
model = pickle.load(open('./models/alzheimer_diagnosis_model.pkl', 'rb'))

st.header('Predição de Alzheimer')
st.write('Este é um modelo de predição de Alzheimer. Para utilizá-lo, preencha os campos abaixo e clique em "Predizer".')

show_data = st.toggle('Mostrar dados e análises', False)
if show_data:
  data_analysis(data)

st.subheader('Insira os valores dos testes abaixo:')
col1, col2, col3= st.columns(3)
with col1:
  st.write('Insira o valor do MMSE (Mini-Mental State Examination) do paciente. O MMSE é um teste de 30 pontos que avalia a cognição do paciente.')
  mmse = st.number_input('MMSE', min_value=0, max_value=30, value=0)

with col2:
  st.write('Insira o valor do Functional Assessment do paciente. O Functional Assessment é um teste de 10 pontos que avalia a funcionalidade do paciente.')
  functional_assessment = st.number_input('Functional Assessment', min_value=0, max_value=10, value=0)

with col3:
  st.write('Insira o valor do ADL (Activities of Daily Living) do paciente. O ADL é um teste de 10 pontos que avalia a capacidade do paciente de realizar atividades diárias.')
  adl = st.number_input('ADL', min_value=0, max_value=10, value=0)
  

st.subheader('Insira as informações abaixo:')
col1, col2 = st.columns(2)
with col1:
  behavioural = st.selectbox('O paciente tem comportamento agressivo?', ['Sim', 'Não'])
  behavioural = 1 if behavioural == 'Sim' else 0

with col2:
  memory_complaint = st.selectbox('O paciente tem queixas de memória?', ['Sim', 'Não'])
  memory_complaint = 1 if memory_complaint == 'Sim' else 0

submit = st.button('Predizer')

values = {}

if submit:
  values = {
    "MMSE": mmse,
    "FunctionalAssessment": functional_assessment,
    "MemoryComplaints": memory_complaint,
    "BehavioralProblems": behavioural,
    "ADL": adl
  }

  values = pd.DataFrame([values])
  print(values)

  results = model.predict(values)
  print(results)

  if len(results) == 1:
    st.subheader('Resultado:')
    st.write('O paciente tem Alzheimer' if results[0] == 1 else 'O paciente não tem Alzheimer')
    