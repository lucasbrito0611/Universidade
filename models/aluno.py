import json
from models.modelo import Modelo

class Aluno:
    def __init__(self, id, nome, matricula, email, telefone, senha, idCurso):
        self.__id = id
        self.__nome = nome
        self.__matricula = matricula
        self.__email = email
        self.__telefone = telefone
        self.__senha = senha
        self.__idCurso = idCurso

    def Set_Id(self, id): self.__id = id
    def Set_Nome(self, nome): self.__nome = nome
    def Set_Matricula(self, matricula): self.__matricula = matricula
    def Set_Email(self, email): self.__email = email
    def Set_Telefone(self, telefone): self.__telefone = telefone
    def Set_Senha(self, senha): self.__senha = senha
    def Set_IdCurso(self, idCurso): self.__idCurso = idCurso

    def Get_Id(self): return self.__id
    def Get_Nome(self): return self.__nome
    def Get_Matricula(self): return self.__matricula
    def Get_Email(self): return self.__email
    def Get_Telefone(self): return self.__telefone
    def Get_Senha(self): return self.__senha
    def Get_IdCurso(self): return self.__idCurso

    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__matricula == x.__matricula and self.__email == x.__email and self.__telefone == x.__telefone and self.__senha == x.__senha and self.__idCurso == x.__idCurso:
            return True
        return False
    
    def __str__(self):
        return f'{self.__id} - {self.__nome} - {self.__matricula} - {self.__email} - {self.__telefone} - {self.__senha} - {self.__idCurso}'
    
class NAluno(Modelo):
    @classmethod
    def ver_matricula_ins(cls, matricula):
        for aluno in cls.objetos:
            if matricula == aluno.Get_Matricula():
                return False
        return True
    
    @classmethod
    def ver_matricula_att(cls, id, matricula):
        for aluno in cls.objetos:
            if matricula == aluno.Get_Matricula() and id != aluno.Get_Id():
                return False
        return True

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open('alunos.json', mode='r') as arquivo:
                alunos_json = json.load(arquivo)
                for obj in alunos_json:
                    aux = Aluno(obj['_Aluno__id'], 
                                obj['_Aluno__nome'], 
                                obj['_Aluno__matricula'],
                                obj['_Aluno__email'],
                                obj['_Aluno__telefone'],
                                obj['_Aluno__senha'],
                                obj['_Aluno__idCurso'])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('alunos.json', mode='w') as arquivo:
            json.dump(cls.objetos, arquivo, default=vars, indent=2)