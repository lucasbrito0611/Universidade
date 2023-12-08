import json

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
    
class NDepartamento:
    __departamentos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for departamento in cls.__departamentos:
            if departamento.Get_Id() > id: id = departamento.Get_Id()

        obj.Set_Id(id + 1)
        cls.__departamentos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__departamentos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for departamento in cls.__departamentos:
            if departamento.Get_Id() == id: return departamento
        return None
    
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.Get_Id())
        if aux is not None:
            aux.Set_Nome(obj.Get_Nome())
            aux.Set_Descricao(obj.Get_Descricao())
            aux.Set_idUniversidade(obj.Get_idUniversidade())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.Get_Id())
        if aux is not None:
            cls.__departamentos.remove(aux)
            cls.salvar()
    
    @classmethod
    def abrir(cls):
        cls.__departamentos = []
        try:
            with open('departamentos.json', mode='r') as arquivo:
                departamentos_json = json.load(arquivo)
                for obj in departamentos_json:
                    aux = Departamento(obj['Id'], 
                            obj['Nome'], 
                            obj['Descrição'],
                            obj['idUniversidade'])
                    cls.__departamentos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('departamentos.json', mode='w') as arquivo:
            json.dump(cls.__departamentos, arquivo, default=vars, indent=2)