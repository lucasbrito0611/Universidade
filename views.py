from models.aluno import Aluno, NAluno
from models.universidade import Universidade, NUniversidade
from models.departamento import Departamento, NDepartamento
from models.curso import Curso, NCurso

class View:
    def Aluno_Listar():
        return NAluno.listar()
    
    def Aluno_ListarId():
        return NAluno.listar_id()

    def Aluno_Inserir(nome, matricula, email, telefone, senha, idCurso):
        if NAluno.ver_matricula_ins(matricula) == False: raise ValueError('Matrícula já cadastrada!')
        NAluno.inserir(Aluno(0, nome, matricula, email, telefone, senha, idCurso))
    
    def Aluno_Atualizar(id, nome, matricula, email, telefone, senha, idCurso):
        if NAluno.ver_matricula_att(id, matricula) == False: raise ValueError('Matrícula já cadastrada!')
        NAluno.atualizar(Aluno(id, nome, matricula, email, telefone, senha, idCurso))

    def Aluno_Excluir(id):
        NAluno.excluir(Aluno(id, '', '', '', '', '', ''))

    def Aluno_Admin():
        for aluno in View.Aluno_Listar():
            if aluno.Get_Nome() == 'admin': return
        View.Aluno_Inserir('admin', 'admin', 'admin', '0000', 'admin', 0)

    def Aluno_Login(matricula, senha):
        if matricula != 'admin':
            for aluno in View.Aluno_Listar():
                if aluno.Get_Matricula() == int(matricula) and aluno.Get_Senha() == senha:
                    return aluno
        else:
            for aluno in View.Aluno_Listar():
                if aluno.Get_Matricula() == matricula and aluno.Get_Senha() == senha:
                    return aluno
        return None
    
    def Univ_Listar():
        return NUniversidade.listar()
    
    def Univ_ListarId():
        return NUniversidade.listar_id()
    
    def Univ_Inserir(nome, localizacao, descricao):
        NUniversidade.inserir(Universidade(0, nome, localizacao, descricao))

    def Univ_Atualizar(id, nome, localizacao, descricao):
        NUniversidade.atualizar(Universidade(id, nome, localizacao, descricao))

    def Univ_Excluir(id):
        NUniversidade.excluir(Universidade(id, '', '', ''))

    def Univ_Informacoes(id):
        departamentos = []
        for departamento in View.Depart_Listar():
            if id == departamento.Get_IdUniversidade():
                departamentos.append(departamento)
        return departamentos

    def Depart_Listar():
        return NDepartamento.listar()
    
    def Depart_ListarId():
        return NDepartamento.listar_id()
    
    def Depart_Inserir(nome, descricao, idUniversidade):
        NDepartamento.inserir(Departamento(0, nome, descricao, idUniversidade))

    def Depart_Atualizar(id, nome, descricao, idUniversidade):
        NDepartamento.atualizar(Departamento(id, nome, descricao, idUniversidade))

    def Depart_Excluir(id):
        NDepartamento.excluir(Departamento(id, '', '', ''))

    def Depart_Informacoes(id):
        cursos = []
        for curso in View.Curso_Listar():
            if id == curso.Get_IdDepartamento():
                cursos.append(curso)
        return cursos

    def Curso_Listar():
        return NCurso.listar()
    
    def Curso_ListarId():
        return NCurso.listar_id()
    
    def Curso_Inserir(nome, descricao, codigo, cargahoraria, idDepartamento):
        if NCurso.ver_codigo_ins(codigo) == False: raise ValueError('Código já cadastrado!')
        NCurso.inserir(Curso(0, nome, descricao, codigo, cargahoraria, idDepartamento))

    def Curso_Atualizar(id, nome, descricao, codigo, cargahoraria, idDepartamento):
        if NCurso.ver_codigo_att(id, codigo) == False: raise ValueError('Código já cadastrado!')
        NCurso.atualizar(Curso(id, nome, descricao, codigo, cargahoraria, idDepartamento))

    def Curso_Excluir(id):
        NCurso.excluir(Curso(id, '', '', '', '', ''))

    def Curso_Informacoes(id):
        alunos = []
        for aluno in View.Aluno_Listar():
            if id == aluno.Get_IdCurso():
                alunos.append(aluno)
        return alunos