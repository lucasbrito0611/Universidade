import streamlit as st
import time

class ManterUnivUI:
    def Main():
        st.header('Cadastro de Universidades')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1: ManterUnivUI.Listar()
        with tab2: ManterUnivUI.Inserir()
        with tab3: ManterUnivUI.Atualizar()
        with tab4: ManterUnivUI.Excluir()

    def Listar():
        st.write('Nenhuma universidade cadastrada ainda')

    def Inserir():
        nome = st.text_input('Informe o nome')
        localizacao = st.text_input('Informe a localização')
        descricao = st.text_input('Digite uma descrição')

        if st.button('Inserir'):
            time.sleep(1)
            st.rerun()
    
    def Atualizar():
        op = st.selectbox('Atualização de Universidades', [])
        localizacao = st.text_input('Informe a nova localização')
        descricao = st.text_input('Digite uma nova descrição')

        if st.button('Atualizar'):
            time.sleep(1)
            st.rerun()

    def Excluir():
        op = st.selectbox('Exclusão de Universidades', [])

        if st.button('Excluir'):
            time.sleep(1)
            st.rerun()