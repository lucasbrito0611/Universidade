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

class IndexUI:
    def Menu():
        op = st.sidebar.selectbox('Menu', ['Login', 'Abrir Conta', 'Manter Universidade', 'Manter Departamento', 'Manter Curso', 'Manter Aluno', 'Visualizar Universidade', 'Visualizar Departamento', 'Visualizar Curso', 'Editar Perfil'])
        if op == 'Login': LoginUI.Main()
        if op == 'Abrir Conta': AbrirContaUI.Main()
        if op == 'Manter Universidade': ManterUnivUI.Main()
        if op == 'Manter Departamento': ManterDepartUI.Main()
        if op == 'Manter Curso': ManterCursoUI.Main()
        if op == 'Manter Aluno': ManterAlunoUI.Main()
        if op == 'Visualizar Universidade': VisualizarUnivUI.Main()
        if op == 'Visualizar Departamento': VisualizarDepartUI.Main()
        if op == 'Visualizar Curso': VisualizarCursoUI.Main()
        if op == 'Editar Perfil': EditarPerfilUI.Main()
    def Logout():
        if st.sidebar.button('Logout'):
            st.rerun()
    def SideBar():
        IndexUI.Menu()
        IndexUI.Logout()

IndexUI.SideBar()