import streamlit as st
import pandas as pd
import time
from views import View

class ManterAlunoUI:
    def Main():
        st.header('Cadastro de Alunos')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1: ManterAlunoUI.Listar()
        with tab2: ManterAlunoUI.Inserir()
        with tab3: ManterAlunoUI.Atualizar()
        with tab4: ManterAlunoUI.Excluir()

    def Listar():
        alunos = View.Aluno_Listar()
        if len(alunos) == 0:
            st.write('Nenhum aluno cadastrado')
        else:
            tabela = []

            for aluno in alunos:
                id = aluno.Get_Id()
                nome = aluno.Get_Nome()
                matricula = aluno.Get_Matricula()
                email = aluno.Get_Email()
                telefone = aluno.Get_Telefone()
                senha = aluno.Get_Senha()
                idCurso = aluno.Get_IdCurso()

                for curso in View.Curso_Listar():
                    if idCurso == curso.Get_Id():
                        idCurso = curso.Get_Nome()

                tabela.append([id, nome, matricula, email, telefone, senha, idCurso])

            df = pd.DataFrame(tabela, columns=['Id', 'Nome', 'Matrícula', 'E-mail', 'Telefone', 'Senha', 'Curso'])

            st.dataframe(df, use_container_width=True)

    def Inserir():
        nome = st.text_input('Informe o nome')
        matricula = st.text_input('Informe a matrícula')
        email = st.text_input('Informe o email')
        telefone = st.text_input('Informe o telefone')
        senha = st.text_input('Informe a senha')
        idCurso = st.selectbox('Selecione o curso', View.Curso_Listar())

        if st.button('Inserir'):
            try:
                View.Aluno_Inserir(nome, int(matricula), email, telefone, senha, idCurso.Get_Id())
                st.success('Aluno inserido com sucesso!')
                time.sleep(1)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
                time.sleep(2)
                st.rerun()
    
    def Atualizar():
        alunos = View.Aluno_Listar()
        if len(alunos) == 0:
            st.write('Nenhum aluno cadastrado')
        else:
            op = st.selectbox('Atualização de Alunos', alunos)
            id = op.Get_Id()
            nome = st.text_input('Informe o novo nome', op.Get_Nome()) 
            matricula = st.text_input('Informe a nova matrícula', op.Get_Matricula())
            email = st.text_input('Informe o novo e-mail', op.Get_Email())
            telefone = st.text_input('Informe o novo telefone', op.Get_Telefone()) 
            senha = st.text_input('Informe a nova senha', op.Get_Senha())
            idCurso = st.selectbox('Selecione o novo curso', View.Curso_Listar())

            if st.button('Atualizar'):
                try:
                    View.Aluno_Atualizar(id, nome, int(matricula), email, telefone, senha, idCurso.Get_Id())
                    st.success('Aluno atualizado com sucesso!')
                    time.sleep(1)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(2)
                    st.rerun()

    def Excluir():
        alunos = View.Aluno_Listar()
        if len(alunos) == 0:
            st.write('Nenhum aluno cadastrado')
        else:
            op = st.selectbox('Exclusão de Alunos', alunos)
            id = op.Get_Id()

            if st.button('Excluir'):
                View.Aluno_Excluir(id)
                st.success('Aluno excluído com sucesso!')
                time.sleep(1)
                st.rerun()