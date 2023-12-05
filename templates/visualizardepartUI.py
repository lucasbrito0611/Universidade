import streamlit as st

class VisualizarDepartUI:
    def Main():
        st.header('Visualizar Departamento')
        VisualizarDepartUI.Listar()

    def Listar():
        #aqui vou colocar a lista dos departamentos
        op = st.selectbox('Selecione o Departamento', [])