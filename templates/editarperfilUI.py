import streamlit as st
import time
from views import View

class EditarPerfilUI:
    def Main():
        st.header('Editar Perfil')
        EditarPerfilUI.Editar()

    def Editar():
        id = st.session_state['aluno_id']

        if st.session_state['aluno_nome'] == 'admin':
            nome = st.session_state['aluno_nome']
            matricula = 'admin'
            email = st.text_input('Informe o novo email')
            telefone = st.text_input('Informe o novo telefone')
            senha = st.text_input('Informe a nova senha')

            if st.button('Editar'):
                View.Aluno_Atualizar(id, nome, matricula, email, telefone, senha, 0)
                st.success('Perfil editado com sucesso!')
                time.sleep(1)
                st.rerun()
        else:
            nome = st.text_input('Informe o novo nome')
            matricula = st.text_input('Informe a nova matrícula')
            email = st.text_input('Informe o novo email')
            telefone = st.text_input('Informe o novo telefone')
            senha = st.text_input('Informe a nova senha')
            idCurso = st.selectbox('Selecione o curso', View.Curso_Listar())

            if st.button('Editar'):
                View.Aluno_Atualizar(id, nome, int(matricula), email, telefone, senha, idCurso.Get_Id())
                st.success('Perfil editado com sucesso!')
                time.sleep(1)
                st.rerun()