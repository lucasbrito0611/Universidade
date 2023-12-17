import streamlit as st
import pandas as pd
import time
from views import View

class ManterCursoUI:
    def Main():
        st.header('Cadastro de Cursos')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1: ManterCursoUI.Listar()
        with tab2: ManterCursoUI.Inserir()
        with tab3: ManterCursoUI.Atualizar()
        with tab4: ManterCursoUI.Excluir()

    def Listar():
        cursos = View.Curso_Listar()
        if len(cursos) == 0:
            st.write('Nenhum curso cadastrado')
        else:
            tabela = []

            for curso in cursos:
                id = curso.Get_Id()
                nome = curso.Get_Nome()
                descricao = curso.Get_Descricao()
                codigo = curso.Get_Codigo()
                cargahoraria = curso.Get_Cargahoraria()
                idDepartamento = curso.Get_IdDepartamento()

                for departamento in View.Depart_Listar():
                    if idDepartamento == departamento.Get_Id():
                        idDepartamento = departamento.Get_Nome()

                tabela.append([id, nome, descricao, codigo, cargahoraria, idDepartamento])

            df = pd.DataFrame(tabela, columns=['Id', 'Nome', 'Descrição', 'Código', 'Carga Horária', 'Departamento'])

            st.dataframe(df, use_container_width=True)

    def Inserir():
        nome = st.text_input('Informe o nome')
        descricao = st.text_input('Digite uma descrição')
        codigo = st.text_input('Informe o código')
        cargahoraria = st.text_input('Informe a carga horária')
        idDepartamento = st.selectbox('Selecione o departamento', View.Depart_Listar())

        if st.button('Inserir'):
            View.Curso_Inserir(nome, descricao, int(codigo), int(cargahoraria), idDepartamento.Get_Id())
            st.success('Curso cadastrado com sucesso!')
            time.sleep(1)
            st.rerun()
    
    def Atualizar():
        cursos = View.Curso_Listar()
        if len(cursos) == 0:
            st.write('Nenhum curso cadastrado')
        else:
            op = st.selectbox('Atualização de Cursos', cursos)
            id = op.Get_Id()
            nome = st.text_input('Informe o novo nome', op.Get_Nome()) 
            descricao = st.text_input('Digite uma nova descrição', op.Get_Descricao())
            codigo = st.text_input('Informe o novo código', op.Get_Codigo())
            cargahoraria = st.text_input('Informe a nova carga horária', op.Get_Cargahoraria())
            idDepartamento = st.selectbox('Selecione o novo departamento', View.Depart_Listar())

            if st.button('Atualizar'):
                View.Curso_Atualizar(id, nome, descricao, int(codigo), int(cargahoraria), idDepartamento.Get_Id())
                st.success('Curso atualizado com sucesso!')
                time.sleep(1)
                st.rerun()

    def Excluir():
        cursos = View.Curso_Listar()
        if len(cursos) == 0:
            st.write('Nenhum curso cadastrado')
        else:
            op = st.selectbox('Exclusão de Cursos', cursos)
            id = op.Get_Id()

            if st.button('Excluir'):
                View.Curso_Excluir(id)
                st.success('Curso excluído com sucesso!')
                time.sleep(1)
                st.rerun()