import streamlit as st
import time
from views import View

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
        idCurso = st.selectbox('Selecione o curso', View.Curso_Listar())

        if st.button('Inserir'):
            View.Aluno_Inserir(nome, int(matricula), email, telefone, senha, idCurso.Get_Id())
            st.success('Conta aberta com sucesso!')
            time.sleep(1)
            st.rerun()