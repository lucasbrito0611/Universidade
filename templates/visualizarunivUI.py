import streamlit as st

class VisualizarUnivUI:
    def Main():
        st.header('Visualizar Universidade')
        VisualizarUnivUI.Listar()

    def Listar():
        #aqui vou colocar a lista das universidades
        op = st.selectbox('Selecione a Universidade', [])