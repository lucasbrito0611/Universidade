import streamlit as st
import time

class ManterCursoUI:
    def Main():
        st.header('Cadastro de Cursos')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1: ManterCursoUI.Listar()
        with tab2: ManterCursoUI.Inserir()
        with tab3: ManterCursoUI.Atualizar()
        with tab4: ManterCursoUI.Excluir()

    def Listar():
        st.write('Nenhum curso cadastrado ainda')

    def Inserir():
        nome = st.text_input('Informe o nome')
        descricao = st.text_input('Digite uma descrição')
        codigo = st.text_input('Informe o código')
        cargahoraria = st.text_input('Informe a carga horária')
        idDepartamento = st.selectbox('Selecione o departamento', [])

        if st.button('Inserir'):
            time.sleep(1)
            st.rerun()
    
    def Atualizar():
        op = st.selectbox('Atualização de Cursos', [])
        nome = st.text_input('Informe o novo nome') 
        descricao = st.text_input('Digite uma nova descrição')
        codigo = st.text_input('Informe o novo código')
        cargahoraria = st.text_input('Informe a nova carga horária')
        idDepartamento = st.selectbox('Selecione o novo departamento', [])

        if st.button('Atualizar'):
            time.sleep(1)
            st.rerun()

    def Excluir():
        op = st.selectbox('Exclusão de Cursos', [])

        if st.button('Excluir'):
            time.sleep(1)
            st.rerun()