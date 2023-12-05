import streamlit as st

class VisualizarCursoUI:
    def Main():
        st.header('Visualizar Curso')
        VisualizarCursoUI.Listar()

    def Listar():
        #aqui vou colocar a lista dos cursos
        op = st.selectbox('Selecione o Curso', [])