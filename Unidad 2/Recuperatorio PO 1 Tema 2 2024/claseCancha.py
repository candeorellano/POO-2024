class Cancha:
    __id:str
    __tipoPiso:str
    __importePorHora:int

    def __init__(self, id, tp, impH):
        self.__id = id
        self.__tipoPiso = tp
        self.__importePorHora = impH

    def getId(self):
        return self.__id
    
    def getTipoPiso(self):
        return self.__tipoPiso
    
    def getImportePorHora(self):
        return self.__importePorHora
    
    def __str__(self):
        return f"Cancha ID: {self.__id}, Tipo de Piso: {self.__tipoPiso}, Importe por Hora: ${self.__importePorHora}"
    
    