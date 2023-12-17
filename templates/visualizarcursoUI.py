import streamlit as st
import pandas as pd
from views import View

class VisualizarCursoUI:
    def Main():
        st.header('Visualizar Curso')
        VisualizarCursoUI.Listar()

    def Listar():
        op = st.selectbox('Selecione o Curso', View.Curso_Listar())
        id = op.Get_Id()

        if st.button('Visualizar'):
            st.write('Nome do Curso:', op.Get_Nome())
            st.write('Descrição do Curso:', op.Get_Descricao())
            st.write('Código do Curso:', str(op.Get_Codigo()))
            st.write('Carga Horária do Curso:', str(op.Get_Cargahoraria()))
            st.write(f'Alunos do Curso {op.Get_Nome()}:')

            alunos = View.Curso_Informacoes(id)
            if len(alunos) == 0:
                st.write('Nenhum aluno cadastrado')
            else:
                tabela = []

                for aluno in alunos:
                    id_Aluno = aluno.Get_Id()
                    nome = aluno.Get_Nome()
                    matricula = str(aluno.Get_Matricula())
                    email = aluno.Get_Email()
                    telefone = aluno.Get_Telefone()
                    senha = aluno.Get_Senha()
                    idCurso = aluno.Get_IdCurso()

                    for curso in View.Curso_Listar():
                        if idCurso == curso.Get_Id():
                            idCurso = curso.Get_Nome()

                    tabela.append([id_Aluno, nome, matricula, email, telefone, senha, idCurso])

                df = pd.DataFrame(tabela, columns=['Id', 'Nome', 'Matrícula', 'E-mail', 'Telefone', 'Senha', 'Curso'])

                st.dataframe(df, use_container_width=True)