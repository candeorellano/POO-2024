import abc
from abc import ABC

class Plan:
    __nombreComp:str
    __duracion:int
    __cobertura:str
    __precioBase:float

    def __init__(self, nomC, dur, cob, precioB):
        self.__nombreComp = nomC
        self.__duracion = dur
        self.__cobertura = cob
        self.__precioBase = precioB

    def getNombreCompania(self):
        return self.__nombreComp
    
    def getDuracion(self):
        return self.__duracion
    
    def getCobertura(self):
        return self.__cobertura
    
    def getPrecioBase(self):
        return self.__precioBase
    
    @abc.abstractmethod
    def getImporteTotal(self):
        pass

    def __str__(self):
        return f"Nombre de la compania: {self.getNombreCompania()}. Duracion del plan: {self.getDuracion()}. Cobertura geografica: {self.getCobertura()}. Importe final: {self.getImporteTotal()}"