import pickle
import pandas as pd
import streamlit as st
import numpy as np

pickle_in = open("diabete.pkl", "rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Previsão de Diabete (TESTE)"

def predict_disease(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    prediction = classifier.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    return prediction

def main():
    # Estilo para o cabeçalho
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Previsor de Diabete (TESTE)</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Entradas do usuário
    Pregnancies = st.number_input("Quantas gravidezes? (se pode ter)", min_value=0, max_value=17, step=1)
    Glucose = st.number_input("Nível de glicose?", min_value=0, max_value=199, step=1)
    BloodPressure = st.number_input("Pressão arterial?", min_value=0, max_value=122, step=1)
    SkinThickness = st.number_input("Espessura da pele?", min_value=0, max_value=99, step=1)
    Insulin = st.number_input("Nível de insulina no sangue?", min_value=0, max_value=846, step=1)
    BMI = st.number_input("Índice de Massa Corporal (IMC)?", min_value=0.0, max_value=67.1, step=0.1)
    DiabetesPedigreeFunction = st.number_input("Função de pedigree de diabetes?", min_value=0.08, max_value=2.42, step=0.01)
    Age = st.number_input("Idade?", min_value=21, max_value=81, step=1)
    
    # Previsão quando o botão for pressionado
    if st.button("Prever"):
        result = predict_disease(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        st.success('Resultado da previsão: {}'.format("Talvez tenha diabete (ISSO É UM TESTE, PODE DAR RESULTADOS NÃO PRECISOS)" if result[0] >= 0.70 else "Talvez não tenha diabete (ISSO É UM TESTE, PODE DAR RESULTADOS NÃO PRECISOS)"))
        print(result)
if __name__ == '__main__':
    main()
