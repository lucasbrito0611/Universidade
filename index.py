import streamlit as st
from templates.manterunivUI import ManterUnivUI
from templates.manterdepartUI import ManterDepartUI
from templates.mantercursoUI import ManterCursoUI
from templates.manteralunoUI import ManterAlunoUI
from templates.abrircontaUI import AbrirContaUI
from templates.visualizarunivUI import VisualizarUnivUI
from templates.visualizardepartUI import VisualizarDepartUI
from templates.visualizarcursoUI import VisualizarCursoUI
from templates.loginUI import LoginUI
from templates.editarperfilUI import EditarPerfilUI
from views import View

class IndexUI:
    def MenuVisitante():
        op = st.sidebar.selectbox('Menu', ['Login', 'Abrir Conta'])
        if op == 'Login': LoginUI.Main()
        if op == 'Abrir Conta': AbrirContaUI.Main()

    def MenuAdmin():
        op = st.sidebar.selectbox('Menu', ['Manter Universidade', 'Manter Departamento', 'Manter Curso', 'Manter Aluno', 'Editar Perfil'])
        if op == 'Manter Universidade': ManterUnivUI.Main()
        if op == 'Manter Departamento': ManterDepartUI.Main()
        if op == 'Manter Curso': ManterCursoUI.Main()
        if op == 'Manter Aluno': ManterAlunoUI.Main()
        if op == 'Editar Perfil': EditarPerfilUI.Main()

    def MenuAluno():
        op = st.sidebar.selectbox('Menu', ['Visualizar Universidade', 'Visualizar Departamento', 'Visualizar Curso', 'Editar Perfil'])
        if op == 'Visualizar Universidade': VisualizarUnivUI.Main()
        if op == 'Visualizar Departamento': VisualizarDepartUI.Main()
        if op == 'Visualizar Curso': VisualizarCursoUI.Main()
        if op == 'Editar Perfil': EditarPerfilUI.Main()

    def Logout():
        if st.sidebar.button('Logout'):
            del st.session_state['aluno_id']
            del st.session_state['aluno_nome']
            st.rerun()
    
    def SideBar():
        if 'aluno_id' not in st.session_state:
            IndexUI.MenuVisitante()
        else:
            if st.session_state['aluno_nome'] != 'admin':
                IndexUI.MenuAluno()
            else:
                IndexUI.MenuAdmin()
            
            st.sidebar.write('Bem-vindo(a), ' + st.session_state['aluno_nome'])
            IndexUI.Logout()
        
        View.Aluno_Admin()

IndexUI.SideBar()