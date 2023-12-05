import streamlit as st
import time

class EditarPerfilUI:
    def Main():
        st.header('Editar Perfil')
        EditarPerfilUI.Editar()

    def Editar():
        nome = st.text_input('Informe o nome')
        matricula = st.text_input('Informe a matrícula')
        email = st.text_input('Informe o email')
        telefone = st.text_input('Informe o telefone')
        senha = st.text_input('Informe a senha')
        idCurso = st.selectbox('Selecione o curso', [])

        if st.button('Editar'):
            time.sleep(1)
            st.rerun()