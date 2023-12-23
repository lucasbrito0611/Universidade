import json
from models.modelo import Modelo

class Departamento:
    def __init__(self, id, nome, descricao, idUniversidade):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__idUniversidade = idUniversidade

    def Set_Id(self, id): self.__id = id
    def Set_Nome(self, nome): self.__nome = nome
    def Set_Descricao(self, descricao): self.__descricao = descricao
    def Set_IdUniversidade(self, idUniversidade): self.__idUniversidade = idUniversidade

    def Get_Id(self): return self.__id
    def Get_Nome(self): return self.__nome
    def Get_Descricao(self): return self.__descricao
    def Get_IdUniversidade(self): return self.__idUniversidade

    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__descricao == x.__descricao and self.__idUniversidade == x.__idUniversidade:
            return True
        return False
    
    def __str__(self):
        return f'{self.__id} - {self.__nome} - {self.__descricao} - {self.__idUniversidade}'
    
class NDepartamento(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open('departamentos.json', mode='r') as arquivo:
                departamentos_json = json.load(arquivo)
                for obj in departamentos_json:
                    aux = Departamento(obj['_Departamento__id'], 
                            obj['_Departamento__nome'], 
                            obj['_Departamento__descricao'],
                            obj['_Departamento__idUniversidade'])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('departamentos.json', mode='w') as arquivo:
            json.dump(cls.objetos, arquivo, default=vars, indent=2)