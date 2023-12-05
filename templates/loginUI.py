import streamlit as st
import time

class LoginUI:
    def Main():
        st.header('Entrar no sistema')
        LoginUI.Entrar()

    def Entrar():
        matricula = st.text_input('Informe a matrícula')
        senha = st.text_input('Informe a senha')

        if st.button('Login'):
            time.sleep(1)
            st.rerun()