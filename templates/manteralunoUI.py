import streamlit as st
import time

class ManterAlunoUI:
    def Main():
        st.header('Cadastro de Alunos')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1: ManterAlunoUI.Listar()
        with tab2: ManterAlunoUI.Inserir()
        with tab3: ManterAlunoUI.Atualizar()
        with tab4: ManterAlunoUI.Excluir()

    def Listar():
        st.write('Nenhum aluno cadastrado ainda')

    def Inserir():
        nome = st.text_input('Informe o nome')
        matricula = st.text_input('Informe a matrícula')
        email = st.text_input('Informe o email')
        telefone = st.text_input('Informe o telefone')
        senha = st.text_input('Informe a senha')
        idCurso = st.selectbox('Selecione o curso', [])

        if st.button('Inserir'):
            time.sleep(1)
            st.rerun()
    
    def Atualizar():
        op = st.selectbox('Atualização de Alunos', [])
        nome = st.text_input('Informe o novo nome') 
        matricula = st.text_input('Informe a nova matrícula')
        email = st.text_input('Informe o novo e-mail')
        telefone = st.text_input('Informe o novo telefone') 
        senha = st.text_input('Informe a nova senha')
        idCurso = st.selectbox('Selecione o novo curso', [])

        if st.button('Atualizar'):
            time.sleep(1)
            st.rerun()

    def Excluir():
        op = st.selectbox('Exclusão de Alunos', [])

        if st.button('Excluir'):
            time.sleep(1)
            st.rerun()