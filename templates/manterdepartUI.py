import streamlit as st
import time

class ManterDepartUI:
    def Main():
        st.header('Cadastro de Departamentos')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1: ManterDepartUI.Listar()
        with tab2: ManterDepartUI.Inserir()
        with tab3: ManterDepartUI.Atualizar()
        with tab4: ManterDepartUI.Excluir()

    def Listar():
        st.write('Nenhum departamento cadastrado ainda')

    def Inserir():
        nome = st.text_input('Informe o nome')
        descrição = st.text_input('Digite uma descrição')
        idUniversidade = st.selectbox('Selecione a universidade', [])

        if st.button('Inserir'):
            time.sleep(1)
            st.rerun()
    
    def Atualizar():
        op = st.selectbox('Atualização de Departamentos', [])
        nome = st.text_input('Informe o novo nome') 
        descrição = st.text_input('Digite uma nova descrição')
        idUniversidade = st.selectbox('Selecione a nova universidade', [])

        if st.button('Atualizar'):
            time.sleep(1)
            st.rerun()

    def Excluir():
        op = st.selectbox('Exclusão de Departamentos', [])

        if st.button('Excluir'):
            time.sleep(1)
            st.rerun()