import streamlit as st
import pandas as pd
import time
from views import View

class ManterDepartUI:
    def Main():
        st.header('Cadastro de Departamentos')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1: ManterDepartUI.Listar()
        with tab2: ManterDepartUI.Inserir()
        with tab3: ManterDepartUI.Atualizar()
        with tab4: ManterDepartUI.Excluir()

    def Listar():
        departamentos = View.Depart_Listar()
        if len(departamentos) == 0:
            st.write('Nenhum departamento cadastrado')
        else:
            tabela = []

            for departamento in departamentos:
                id = departamento.Get_Id()
                nome = departamento.Get_Nome()
                descricao = departamento.Get_Descricao()
                idUniversidade = departamento.Get_IdUniversidade()

                for universidade in View.Univ_Listar():
                    if idUniversidade == universidade.Get_Id():
                        idUniversidade = universidade.Get_Nome()

                tabela.append([id, nome, descricao, idUniversidade])

            df = pd.DataFrame(tabela, columns=['Id', 'Nome', 'Descrição', 'Universidade'])

            st.dataframe(df, use_container_width=True)

    def Inserir():
        nome = st.text_input('Informe o nome')
        descricao = st.text_input('Digite uma descrição')
        idUniversidade = st.selectbox('Selecione a universidade', View.Univ_Listar())

        if st.button('Inserir'):
            View.Depart_Inserir(nome, descricao, idUniversidade.Get_Id())
            st.success('Departamento inserido com sucesso!')
            time.sleep(1)
            st.rerun()
    
    def Atualizar():
        departamentos = View.Depart_Listar()
        if len(departamentos) == 0:
            st.write('Nenhum departamento cadastrado')
        else:
            op = st.selectbox('Atualização de Departamentos', departamentos)
            id = op.Get_Id()
            nome = st.text_input('Informe o novo nome', op.Get_Nome()) 
            descricao = st.text_input('Digite uma nova descrição', op.Get_Descricao())
            idUniversidade = st.selectbox('Selecione a nova universidade', View.Univ_Listar())

            if st.button('Atualizar'):
                View.Depart_Atualizar(id, nome, descricao, idUniversidade.Get_Id())
                st.success('Departamento atualizado com sucesso!')
                time.sleep(1)
                st.rerun()

    def Excluir():
        departamentos = View.Depart_Listar()
        if len(departamentos) == 0:
            st.write('Nenhum departamento cadastrado')
        else:
            op = st.selectbox('Exclusão de Departamentos', departamentos)
            id = op.Get_Id()

        if st.button('Excluir'):
            View.Depart_Excluir(id)
            st.success('Departamento excluído com sucesso!')
            time.sleep(1)
            st.rerun()