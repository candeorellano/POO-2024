from clasePlan import Plan

class PlanTelevision(Plan):
    __cantCanalesNacionales:int
    __cantCanalesInternacionales:int

    def __init__(self, nomC, dur, cob, precioB, cantNac, cantInternac):
        super().__init__(nomC, dur, cob, precioB)
        self.__cantCanalesNacionales = cantNac
        self.__cantCanalesInternacionales = cantInternac

    def getCantCanalesNacionales(self):
        return self.__cantCanalesNacionales
    
    def getCantCanalesInternacionales(self):
        return self.__cantCanalesInternacionales
    
    def getImporteTotal(self):
        base = self.getPrecioBase()
        importe = self.getPrecioBase()

        if self.__cantCanalesInternacionales > 10:
            importe += ((base*15)/100)
        return importe
