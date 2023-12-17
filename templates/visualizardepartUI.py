import streamlit as st
import pandas as pd
from views import View

class VisualizarDepartUI:
    def Main():
        st.header('Visualizar Departamento')
        VisualizarDepartUI.Listar()

    def Listar():
        op = st.selectbox('Selecione o Departamento', View.Depart_Listar())
        id = op.Get_Id()

        if st.button('Visualizar'):
            st.write('Nome do departamento:', op.Get_Nome())
            st.write('Descrição do departamento:', op.Get_Descricao())
            st.write(f'Cursos do Departamento {op.Get_Nome()}:')

            cursos = View.Depart_Informacoes(id)
            if len(cursos) == 0:
                st.write('Nenhum curso cadastrado')
            else:
                tabela = []

                for curso in cursos:
                    id_Curso = curso.Get_Id()
                    nome = curso.Get_Nome()
                    descricao = curso.Get_Descricao()
                    codigo = curso.Get_Codigo()
                    cargahoraria = curso.Get_Cargahoraria()
                    idDepartamento = curso.Get_IdDepartamento()

                    for departamento in View.Depart_Listar():
                        if idDepartamento == departamento.Get_Id():
                            idDepartamento = departamento.Get_Nome()

                    tabela.append([id_Curso, nome, descricao, codigo, cargahoraria, idDepartamento])

                df = pd.DataFrame(tabela, columns=['Id', 'Nome', 'Descrição', 'Código', 'Carga Horária', 'Departamento'])

                st.dataframe(df, use_container_width=True)
