import streamlit as st
import pandas as pd
from views import View

class VisualizarUnivUI:
    def Main():
        st.header('Visualizar Universidade')
        VisualizarUnivUI.Listar()

    def Listar():
        op = st.selectbox('Selecione a Universidade', View.Univ_Listar())
        id = op.Get_Id()

        if st.button('Visualizar'):
            st.write('Nome da universidade:', op.Get_Nome())
            st.write('Localização da universidade:', op.Get_Localizacao())
            st.write('Descrição da universidade:', op.Get_Descricao())
            st.write(f'Departamentos da Universidade {op.Get_Nome()}:')

            departamentos = View.Univ_Informacoes(id)
            if len(departamentos) == 0:
                st.write('Nenhum departamento cadastrado')
            else:
                tabela = []

                for departamento in departamentos:
                    id_Depart = departamento.Get_Id()
                    nome = departamento.Get_Nome()
                    descricao = departamento.Get_Descricao()
                    idUniversidade = departamento.Get_IdUniversidade()

                    for universidade in View.Univ_Listar():
                        if idUniversidade == universidade.Get_Id():
                            idUniversidade = universidade.Get_Nome()

                    tabela.append([id_Depart, nome, descricao, idUniversidade])

                df = pd.DataFrame(tabela, columns=['Id', 'Nome', 'Descrição', 'Universidade'])

                st.dataframe(df, use_container_width=True)