import json
from models.modelo import Modelo

class Curso:
    def __init__(self, id, nome, descricao, codigo, cargahoraria, idDepartamento):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__codigo = codigo
        self.__cargahoraria = cargahoraria
        self.__idDepartamento = idDepartamento

    def Set_Id(self, id): self.__id = id
    def Set_Nome(self, nome): self.__nome = nome
    def Set_Descricao(self, descricao): self.__descricao = descricao
    def Set_Codigo(self, codigo): self.__codigo = codigo
    def Set_Cargahoraria(self, cargahoraria): self.__cargahoraria = cargahoraria
    def Set_IdDepartamento(self, idDepartamento): self.__idDepartamento = idDepartamento

    def Get_Id(self): return self.__id
    def Get_Nome(self): return self.__nome
    def Get_Descricao(self): return self.__descricao
    def Get_Codigo(self): return self.__codigo
    def Get_Cargahoraria(self): return self.__cargahoraria
    def Get_IdDepartamento(self): return self.__idDepartamento

    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__descricao == x.__descricao and self.__codigo == x.__codigo and self.__cargahoraria == x.__cargahoraria and self.__idDepartamento == x.__idDepartamento:
            return True
        return False
    
    def __str__(self):
        return f'{self.__id} - {self.__nome} - {self.__descricao} - {self.__codigo} - {self.__cargahoraria} - {self.__idDepartamento}'
    

class NCurso(Modelo):
    @classmethod
    def ver_codigo_ins(cls, codigo):
        for curso in cls.objetos:
            if codigo == curso.Get_Codigo():
                return False
        return True
    
    @classmethod
    def ver_codigo_att(cls, id, codigo):
        for curso in cls.objetos:
            if codigo == curso.Get_Codigo() and id != curso.Get_Id():
                return False
        return True

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open('cursos.json', mode='r') as arquivo:
                cursos_json = json.load(arquivo)
                for obj in cursos_json:
                    aux = Curso(obj['_Curso__id'], 
                                obj['_Curso__nome'], 
                                obj['_Curso__descricao'],
                                obj['_Curso__codigo'],
                                obj['_Curso__cargahoraria'],
                                obj['_Curso__idDepartamento'])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('cursos.json', mode='w') as arquivo:
            json.dump(cls.objetos, arquivo, default=vars, indent=2)