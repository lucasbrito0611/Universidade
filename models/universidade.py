import json
from models.modelo import Modelo

class Universidade:
    def __init__(self, id, nome, localizacao, descricao):
        self.__id = id
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao

    def Set_Id(self, id): self.__id = id
    def Set_Nome(self, nome): self.__nome = nome
    def Set_Localizacao(self, localizacao): self.__localizacao = localizacao
    def Set_Descricao(self, descricao): self.__descricao = descricao

    def Get_Id(self): return self.__id
    def Get_Nome(self): return self.__nome
    def Get_Localizacao(self): return self.__localizacao
    def Get_Descricao(self): return self.__descricao

    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__localizacao == x.__localizacao and self.__descricao == x.__descricao:
            return True
        return False
    
    def __str__(self):
        return f'{self.__id} - {self.__nome} - {self.__localizacao} - {self.__descricao}'
    
class NUniversidade(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open('universidades.json', mode='r') as arquivo:
                universidades_json = json.load(arquivo)
                for obj in universidades_json:
                    aux = Universidade(obj['_Universidade__id'], 
                            obj['_Universidade__nome'], 
                            obj['_Universidade__localizacao'],
                            obj['_Universidade__descricao'])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('universidades.json', mode='w') as arquivo:
            json.dump(cls.objetos, arquivo, default=vars, indent=2)