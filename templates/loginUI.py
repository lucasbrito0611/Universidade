import streamlit as st
import time
from views import View

class LoginUI:
    def Main():
        st.header('Entrar no sistema')
        LoginUI.Entrar()

    def Entrar():
        matricula = st.text_input('Informe a matrícula')
        senha = st.text_input('Informe a senha')

        if st.button('Login'):
            aluno = View.Aluno_Login(matricula, senha)
            if aluno is not None:
                st.success('Login realizado com sucesso!')
                st.success('Bem-vindo(a), ' + aluno.Get_Nome())
                st.session_state['aluno_id'] = aluno.Get_Id()
                st.session_state['aluno_nome'] = aluno.Get_Nome()
            else:
                st.error('Usuário ou senha inválido(s)')
            time.sleep(2)
            st.rerun()