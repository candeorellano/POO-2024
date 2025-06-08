from clasePlan import Plan

class PlanTelefonia(Plan):
    __tipoLlamada:str
    __cantMinutos:int

    def __init__(self, nomC, dur, cob, precioB, tipo, cant):
        super().__init__(nomC, dur, cob, precioB)
        self.__tipoLlamada = tipo
        self.__cantMinutos = cant
    
    def getTipoLlamada(self):
        return self.__tipoLlamada
    
    def getCantMinutos(self):
        return self.__cantMinutos
    
    def getImporteTotal(self):
        base = self.getPrecioBase()
        importe = self.getPrecioBase()
        
        if self.__tipoLlamada == "Nacional e Internacional":
            importe += ((base*20)/100)
        elif self.__tipoLlamada == "Regional":
            importe -= ((base*7.5)/100)
        return importe