import streamlit as st
import pandas as pd
import time
from views import View

class ManterUnivUI:
    def Main():
        st.header('Cadastro de Universidades')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1: ManterUnivUI.Listar()
        with tab2: ManterUnivUI.Inserir()
        with tab3: ManterUnivUI.Atualizar()
        with tab4: ManterUnivUI.Excluir()

    def Listar():
        universidades = View.Univ_Listar()
        if len(universidades) == 0:
            st.write('Nenhuma universidade cadastrada')
        else:
            dic = []
            for obj in universidades: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def Inserir():
        nome = st.text_input('Informe o nome')
        localizacao = st.text_input('Informe a localização')
        descricao = st.text_input('Digite uma descrição')

        if st.button('Inserir'):
            View.Univ_Inserir(nome, localizacao, descricao)
            st.success('Universidade inserida com sucesso!')
            time.sleep(1)
            st.rerun()
    
    def Atualizar():
        universidades = View.Univ_Listar()
        if len(universidades) == 0:
            st.write('Nenhuma universidade cadastrada')
        else:
            op = st.selectbox('Atualização de Universidades', universidades)
            id = op.Get_Id()
            nome = st.text_input('Informe o novo nome', op.Get_Nome())
            localizacao = st.text_input('Informe a nova localização', op.Get_Localizacao())
            descricao = st.text_input('Digite uma nova descrição', op.Get_Descricao())

            if st.button('Atualizar'):
                View.Univ_Atualizar(id, nome, localizacao, descricao)
                st.success('Universidade atualizada com sucesso!')
                time.sleep(1)
                st.rerun()

    def Excluir():
        universidades = View.Univ_Listar()
        if len(universidades) == 0:
            st.write('Nenhuma universidade cadastrada')
        else:
            op = st.selectbox('Exclusão de Universidades', universidades)
            id = op.Get_Id()
            
            if st.button('Excluir'):
                View.Univ_Excluir(id)
                st.success('Universidade excluída com sucesso!')
                time.sleep(1)
                st.rerun()