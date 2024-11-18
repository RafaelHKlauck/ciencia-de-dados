import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
import plotly.express as px

positive_diagnosis = None
negative_diagnosis = None

def get_column_values_means(column_name):
  positive_diagnosis_mean = positive_diagnosis[column_name].mean()
  negative_diagnosis_mean = negative_diagnosis[column_name].mean()
  return positive_diagnosis_mean, negative_diagnosis_mean

def generate_chart(mean1, mean2, title, ylabel, ax):
  sns.barplot(x=['Positive', 'Negative'], y=[mean1, mean2], ax=ax)
  ax.set_title(title, fontsize=10)
  ax.set_xlabel('Diagnóstico', fontsize=8)
  ax.set_ylabel(ylabel, fontsize=8)
  ax.tick_params(axis='x', labelsize=8)
  ax.tick_params(axis='y', labelsize=8)

def generate_demographic_details_charts():
  st.subheader('Detalhes Demográficos')
  p_age_mean, n_age_mean = get_column_values_means('Age')
  p_gender_mean, n_gender_mean = get_column_values_means('Gender')
  p_ethnicity_mean, n_ethnicity_mean = get_column_values_means('Ethnicity')
  p_education_level_mean, n_education_level_mean = get_column_values_means('EducationLevel')

  fig, axs = plt.subplots(2, 2, figsize=(10, 6))
  generate_chart(
    p_age_mean, n_age_mean, 
    'Média de idade por diagnóstico', 
    'Média de idade', 
    ax=axs[0, 0]
  )
  generate_chart(
    p_gender_mean, n_gender_mean, 
    'Média de gênero por diagnóstico', 
    'Média de gênero', 
    ax=axs[0, 1]
  )
  generate_chart(
    p_ethnicity_mean, n_ethnicity_mean, 
    'Média de etnia por diagnóstico', 
    'Média de etnia', 
    ax=axs[1, 0]
  )
  generate_chart(
    p_education_level_mean, n_education_level_mean, 
    'Média de nível de educação por diagnóstico', 
    'Média de nível de educação', 
    ax=axs[1, 1]
  )
  fig.subplots_adjust(hspace=0.6, wspace=0.6)
  plt.tight_layout()
  st.pyplot(fig) 
  
def generate_life_style_factors_charts(): 
  st.subheader('Fatores de Estilo de Vida')
  p_bmi_mean, n_bmi_mean = get_column_values_means('BMI')
  p_smoking_mean, n_smoking_mean = get_column_values_means('Smoking')
  p_alcohol_consumption_mean, n_alcohol_consumption_mean = get_column_values_means('AlcoholConsumption')
  p_physical_activity_mean, n_physical_activity_mean = get_column_values_means('PhysicalActivity')
  p_diet_quality_mean, n_diet_quality_mean = get_column_values_means('DietQuality')
  p_sleep_quality_mean, n_sleep_quality_mean = get_column_values_means('SleepQuality')

  fig, axs = plt.subplots(2, 3, figsize=(10, 6))
  generate_chart(
    p_bmi_mean, n_bmi_mean, 
    'Média de BMI por diagnóstico', 
    'Média de BMI', 
    ax=axs[0, 0]
  )
  generate_chart(
    p_smoking_mean, n_smoking_mean, 
    'Média de fumantes por diagnóstico', 
    'Média de fumantes', 
    ax=axs[0, 1]
  )
  generate_chart(
    p_alcohol_consumption_mean, n_alcohol_consumption_mean, 
    'Média de consumo de álcool por diagnóstico', 
    'Média de consumo de álcool', 
    ax=axs[0, 2]
  )
  generate_chart(
    p_physical_activity_mean, n_physical_activity_mean, 
    'Média de atividade física por diagnóstico', 
    'Média de atividade física', 
    ax=axs[1, 0]
  )
  generate_chart(
    p_diet_quality_mean, n_diet_quality_mean, 
    'Média de qualidade da dieta por diagnóstico', 
    'Média de qualidade da dieta', 
    ax=axs[1, 1]
  )
  generate_chart(
    p_sleep_quality_mean, n_sleep_quality_mean, 
    'Média de qualidade do sono por diagnóstico', 
    'Média de qualidade do sono', 
    ax=axs[1, 2]
  )
  fig.subplots_adjust(hspace=0.6, wspace=0.6)
  plt.tight_layout()

  st.pyplot(fig)


def generate_medical_history_charts():
  st.subheader('Histórico Médico')
  p_family_history_alzheimers_mean, n_family_history_alzheimers_mean = get_column_values_means('FamilyHistoryAlzheimers')
  p_cardiovascular_disease_mean, n_cardiovascular_disease_mean = get_column_values_means('CardiovascularDisease')
  p_diabetes_mean, n_diabetes_mean = get_column_values_means('Diabetes')
  p_depression_mean, n_depression_mean = get_column_values_means('Depression')
  p_head_injury_mean, n_head_injury_mean = get_column_values_means('HeadInjury')
  p_hypertension_mean, n_hypertension_mean = get_column_values_means('Hypertension')

  fig, axs = plt.subplots(2, 3, figsize=(15, 6))
  generate_chart(
    p_family_history_alzheimers_mean, n_family_history_alzheimers_mean, 
    'Média de histórico familiar de Alzheimer por diagnóstico', 
    'Média de histórico familiar de Alzheimer', 
    ax=axs[0, 0]
  )
  generate_chart(
    p_cardiovascular_disease_mean, n_cardiovascular_disease_mean, 
    'Média de doença cardiovascular por diagnóstico', 
    'Média de doença cardiovascular', 
    ax=axs[0, 1]
  )
  generate_chart(
    p_diabetes_mean, n_diabetes_mean, 
    'Média de diabetes por diagnóstico', 
    'Média de diabetes', 
    ax=axs[0, 2]
  )
  generate_chart(
    p_depression_mean, n_depression_mean, 
    'Média de depressão por diagnóstico', 
    'Média de depressão', 
    ax=axs[1, 0]
  )
  generate_chart(
    p_head_injury_mean, n_head_injury_mean, 
    'Média de lesão na cabeça por diagnóstico', 
    'Média de lesão na cabeça', 
    ax=axs[1, 1]
  )
  generate_chart(
    p_hypertension_mean, n_hypertension_mean, 
    'Média de hipertensão por diagnóstico', 
    'Média de hipertensão', 
    ax=axs[1, 2]
  )
  fig.subplots_adjust(hspace=0.6, wspace=0.6)
  plt.tight_layout()

  st.pyplot(fig)

def clinical_history_charts():
  st.subheader('Histórico Clínico')
  p_systolic_bp_mean, n_systolic_bp_mean = get_column_values_means('SystolicBP')
  p_diastolic_bp_mean, n_diastolic_bp_mean = get_column_values_means('DiastolicBP')
  p_cholesterol_total_mean, n_cholesterol_total_mean = get_column_values_means('CholesterolTotal')
  p_cholesterol_ldl_mean, n_cholesterol_ldl_mean = get_column_values_means('CholesterolLDL')
  p_cholesterol_hdl_mean, n_cholesterol_hdl_mean = get_column_values_means('CholesterolHDL')
  p_cholesterol_triglycerides_mean, n_cholesterol_triglycerides_mean = get_column_values_means('CholesterolTriglycerides')

  fig, axs = plt.subplots(2, 3, figsize=(15, 6))
  generate_chart(
    p_systolic_bp_mean, n_systolic_bp_mean, 
    'Média de pressão sistólica por diagnóstico', 
    'Média de pressão sistólica', 
    ax=axs[0, 0]
  )
  generate_chart(
    p_diastolic_bp_mean, n_diastolic_bp_mean, 
    'Média de pressão diastólica por diagnóstico', 
    'Média de pressão diastólica', 
    ax=axs[0, 1]
  )
  generate_chart(
    p_cholesterol_total_mean, n_cholesterol_total_mean, 
    'Média de colesterol total por diagnóstico', 
    'Média de colesterol total', 
    ax=axs[0, 2]
  )
  generate_chart(
    p_cholesterol_ldl_mean, n_cholesterol_ldl_mean, 
    'Média de colesterol LDL por diagnóstico', 
    'Média de colesterol LDL', 
    ax=axs[1, 0]
  )
  generate_chart(
    p_cholesterol_hdl_mean, n_cholesterol_hdl_mean, 
    'Média de colesterol HDL por diagnóstico', 
    'Média de colesterol HDL', 
    ax=axs[1, 1]
  )
  generate_chart(
    p_cholesterol_triglycerides_mean, n_cholesterol_triglycerides_mean, 
    'Média de colesterol triglicerídeos por diagnóstico', 
    'Média de colesterol triglicerídeos', 
    ax=axs[1, 2]
  )
  fig.subplots_adjust(hspace=0.6, wspace=0.6)
  plt.tight_layout()

  st.pyplot(fig)

def cognitive_assessment_charts():
  st.subheader('Avaliação Cognitiva')
  p_mmse_mean, n_mmse_mean = get_column_values_means('MMSE')
  p_functional_assessment_mean, n_functional_assessment_mean = get_column_values_means('FunctionalAssessment')
  p_memory_complaints_mean, n_memory_complaints_mean = get_column_values_means('MemoryComplaints')
  p_behavioral_problems_mean, n_behavioral_problems_mean = get_column_values_means('BehavioralProblems')
  p_adl_mean, n_adl_mean = get_column_values_means('ADL')

  fig, axs = plt.subplots(2, 3, figsize=(15, 6))
  generate_chart(
    p_mmse_mean, n_mmse_mean, 
    'Média de MMSE por diagnóstico', 
    'Média de MMSE', 
    ax=axs[0, 0]
  )
  generate_chart(
    p_functional_assessment_mean, n_functional_assessment_mean, 
    'Média de avaliação funcional por diagnóstico', 
    'Média de avaliação funcional', 
    ax=axs[0, 1]
  )
  generate_chart(
    p_memory_complaints_mean, n_memory_complaints_mean, 
    'Média de queixas de memória por diagnóstico', 
    'Média de queixas de memória', 
    ax=axs[0, 2]
  )
  generate_chart(
    p_behavioral_problems_mean, n_behavioral_problems_mean, 
    'Média de problemas comportamentais por diagnóstico', 
    'Média de problemas comportamentais', 
    ax=axs[1, 0]
  )
  generate_chart(
    p_adl_mean, n_adl_mean, 
    'Média de ADL por diagnóstico', 
    'Média de ADL', 
    ax=axs[1, 1]
  )
  fig.delaxes(axs[1, 2])
  fig.subplots_adjust(hspace=0.6, wspace=0.6)
  plt.tight_layout()

  st.pyplot(fig)

def symptoms_charts():
  st.subheader('Sintomas')
  p_confusion_mean, n_confusion_mean = get_column_values_means('Confusion')
  p_disorientation_mean, n_disorientation_mean = get_column_values_means('Disorientation')
  p_personality_changes_mean, n_personality_changes_mean = get_column_values_means('PersonalityChanges')
  p_difficulty_completing_tasks_mean, n_difficulty_completing_tasks_mean = get_column_values_means('DifficultyCompletingTasks')
  p_forgetfulness_mean, n_forgetfulness_mean = get_column_values_means('Forgetfulness')

  fig, axs = plt.subplots(2, 3, figsize=(15, 6))
  generate_chart(
    p_confusion_mean, n_confusion_mean, 
    'Média de confusão por diagnóstico', 
    'Média de confusão', 
    ax=axs[0, 0]
  )
  generate_chart(
    p_disorientation_mean, n_disorientation_mean, 
    'Média de desorientação por diagnóstico', 
    'Média de desorientação', 
    ax=axs[0, 1]
  )
  generate_chart(
    p_personality_changes_mean, n_personality_changes_mean, 
    'Média de mudanças de personalidade por diagnóstico', 
    'Média de mudanças de personalidade', 
    ax=axs[0, 2]
  )
  generate_chart(
    p_difficulty_completing_tasks_mean, n_difficulty_completing_tasks_mean, 
    'Média de dificuldade em completar tarefas por diagnóstico', 
    'Média de dificuldade em completar tarefas', 
    ax=axs[1, 0]
  )
  generate_chart(
    p_forgetfulness_mean, n_forgetfulness_mean, 
    'Média de esquecimento por diagnóstico', 
    'Média de esquecimento', 
    ax=axs[1, 1]
  )
  fig.delaxes(axs[1, 2])
  fig.subplots_adjust(hspace=0.6, wspace=0.6)
  plt.tight_layout()

  st.pyplot(fig)

def tree_map_chart(alzheimers_data: DataFrame):
  mean_MMSE = alzheimers_data['MMSE'].mean()
  mean_FunctionalAssessment = alzheimers_data['FunctionalAssessment'].mean()
  mean_ADL = alzheimers_data['ADL'].mean()
  alzheimer_data_for_treemap = alzheimers_data[['Diagnosis', 'MMSE', 'FunctionalAssessment', 'ADL', 'BehavioralProblems', 'MemoryComplaints', 'Gender']].copy()

  # Explicitamente alterando os tipos das colunas para evitar o erro
  alzheimer_data_for_treemap['MMSE'] = alzheimer_data_for_treemap['MMSE'].astype('object')
  alzheimer_data_for_treemap['FunctionalAssessment'] = alzheimer_data_for_treemap['FunctionalAssessment'].astype('object')
  alzheimer_data_for_treemap['ADL'] = alzheimer_data_for_treemap['ADL'].astype('object')
  alzheimer_data_for_treemap['BehavioralProblems'] = alzheimer_data_for_treemap['BehavioralProblems'].astype('object')
  alzheimer_data_for_treemap['MemoryComplaints'] = alzheimer_data_for_treemap['MemoryComplaints'].astype('object')
  alzheimer_data_for_treemap['Gender'] = alzheimer_data_for_treemap['Gender'].astype('object')

  # Aplicando transformações
  alzheimer_data_for_treemap.loc[:, 'MMSE'] = alzheimer_data_for_treemap['MMSE'].apply(
      lambda x: 'MMSE Acima da Média' if x > mean_MMSE else 'MMSE Abaixo da Média'
  )
  alzheimer_data_for_treemap.loc[:, 'FunctionalAssessment'] = alzheimer_data_for_treemap['FunctionalAssessment'].apply(
      lambda x: 'FunctionalAssessment Acima da Média' if x > mean_FunctionalAssessment else 'FunctionalAssessment Abaixo da Média'
  )
  alzheimer_data_for_treemap.loc[:, 'ADL'] = alzheimer_data_for_treemap['ADL'].apply(
      lambda x: 'ADL Acima da Média' if x > mean_ADL else 'ADL Abaixo da Média'
  )
  alzheimer_data_for_treemap.loc[:, 'BehavioralProblems'] = alzheimer_data_for_treemap['BehavioralProblems'].map({0: 'Sem problema de comportamento', 1: 'Com problema de comportamento'})
  alzheimer_data_for_treemap.loc[:, 'MemoryComplaints'] = alzheimer_data_for_treemap['MemoryComplaints'].map({0: 'Sem queixa de falta de memória', 1: 'Com de falta queixa de memória'})
  alzheimer_data_for_treemap.loc[:, 'Gender'] = alzheimer_data_for_treemap['Gender'].map({0: 'Feminino', 1: 'Masculino'})


  fig = px.treemap(
    alzheimer_data_for_treemap,
    path=['MemoryComplaints', 'BehavioralProblems', 'MMSE', 'FunctionalAssessment', 'ADL', 'Gender'],
    title='Treemap de Diagnóstico de Alzheimer com Médias de Categorias',
    color='Diagnosis',
    color_continuous_scale='Viridis'
  )
  st.plotly_chart(fig)

def data_analysis(alzheimers_data: DataFrame):
  st.dataframe(alzheimers_data)
  global positive_diagnosis
  global negative_diagnosis
  positive_diagnosis = alzheimers_data[alzheimers_data['Diagnosis'] == 1]
  negative_diagnosis = alzheimers_data[alzheimers_data['Diagnosis'] == 0]
  generate_demographic_details_charts()
  generate_life_style_factors_charts()
  generate_medical_history_charts()
  clinical_history_charts()
  cognitive_assessment_charts()
  symptoms_charts()
  st.write("Analisando os gráficos, é possível observar que as médias dos dados da sessão Avaliação Cognitiva são bem distintas entre os diagnósticos positivos e negativos. Além disso, o treemap abaixo mostra a distribuição dos diagnósticos de Alzheimer com base nas médias de categorias.")
  tree_map_chart(alzheimers_data)
  st.write("Portanto, é possível concluir que a Avaliação Cognitiva é um fator importante para a predição de Alzheimer.")
