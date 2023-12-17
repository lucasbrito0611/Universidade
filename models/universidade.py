import json

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
    
class NUniversidade:
    __universidades = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for universidade in cls.__universidades:
            if universidade.Get_Id() > id: id = universidade.Get_Id()

        obj.Set_Id(id + 1)
        cls.__universidades.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__universidades
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for universidade in cls.__universidades:
            if universidade.Get_Id() == id: return universidade
        return None
    
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.Get_Id())
        if aux is not None:
            aux.Set_Nome(obj.Get_Nome())
            aux.Set_Localizacao(obj.Get_Localizacao())
            aux.Set_Descricao(obj.Get_Descricao())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.Get_Id())
        if aux is not None:
            cls.__universidades.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__universidades = []
        try:
            with open('universidades.json', mode='r') as arquivo:
                universidades_json = json.load(arquivo)
                for obj in universidades_json:
                    aux = Universidade(obj['_Universidade__id'], 
                            obj['_Universidade__nome'], 
                            obj['_Universidade__localizacao'],
                            obj['_Universidade__descricao'])
                    cls.__universidades.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('universidades.json', mode='w') as arquivo:
            json.dump(cls.__universidades, arquivo, default=vars, indent=2)