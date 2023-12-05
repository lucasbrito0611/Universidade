import streamlit as st
import time

class AbrirContaUI:
    def Main():
        st.header('Abrir conta no sistema')
        AbrirContaUI.Inserir()

    def Inserir():
        nome = st.text_input('Informe o nome')
        matricula = st.text_input('Informe a matrícula')
        email = st.text_input('Informe o email')
        telefone = st.text_input('Informe o telefone')
        senha = st.text_input('Informe a senha')
        idCurso = st.selectbox('Selecione o curso', [])

        if st.button('Inserir'):
            time.sleep(1)
            st.rerun()