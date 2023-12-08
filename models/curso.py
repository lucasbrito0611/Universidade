import json

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
    

class NCurso:
    __cursos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for curso in cls.__cursos:
            if curso.Get_Id() > id: id = curso.Get_Id()

        obj.Set_Id(id + 1)
        cls.__cursos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__cursos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for curso in cls.__cursos:
            if curso.Get_Id() == id: return curso
        return None
    
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.Get_Id())
        if aux is not None:
            aux.Set_Nome(obj.Get_Nome())
            aux.Set_Descricao(obj.Get_Descricao())
            aux.Set_Codigo(obj.Get_Codigo())
            aux.Set_Cargahoraria(obj.Get_Cargahoraria())
            aux.Set_IdDepartamento(obj.Get_IdDepartamento())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.Get_Id())
        if aux is not None:
            cls.__cursos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__cursos = []
        try:
            with open('cursos.json', mode='r') as arquivo:
                cursos_json = json.load(arquivo)
                for obj in cursos_json:
                    aux = Curso(obj['Id'], 
                            obj['Nome'], 
                            obj['Descrição'],
                            obj['Código'],
                            obj['Carga Horária'],
                            obj['idDepartamento'])
                    cls.__cursos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('cursos.json', mode='w') as arquivo:
            json.dump(cls.__cursos, arquivo, default=vars, indent=2)