from abc import ABC, abstractclassmethod

class Modelo(ABC):
    objetos = []

    @classmethod
    def inserir(cls, obj):
      cls.abrir()
      id = 0
      for aux in cls.objetos:
        if aux.Get_Id() > id: id = aux.Get_Id()
        obj.Set_Id(id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.Get_Id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.Get_Id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.Get_Id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.salvar()

    @abstractclassmethod
    def abrir(cls):
        pass

    @abstractclassmethod
    def salvar(cls):
        pass