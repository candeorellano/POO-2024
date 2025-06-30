class Alquiler:
    __nombre:str
    __idCancha:str
    __hora:int
    __minutos:int
    __duracion:int

    def __init__(self, nombre, idCancha, hora, minutos, duracion):
        self.__nombre = nombre
        self.__idCancha = idCancha
        self.__hora = hora
        self.__minutos = minutos
        self.__duracion = duracion

    def getNombre(self):
        return self.__nombre
    
    def getIdCancha(self):
        return self.__idCancha
    
    def getHora(self):
        return self.__hora
    
    def getMinutos(self):
        return self.__minutos
    
    def getDuracion(self):
        return self.__duracion

    def __str__(self):
        return f"Alquiler: {self.__nombre}, ID Cancha: {self.__idCancha}, Hora: {self.__hora}:{self.__minutos}, Duración: {self.__duracion} minutos"
    
    def __gt__(self, otro):
        retorno = None
        # Primero comparamos las horas
        if self.getHora() > otro.getHora():
            retorno = True
        elif self.getHora() < otro.getHora():
            retorno = False
        else:  # Las horas son iguales, comparamos los minutos
            retorno = self.getMinutos() > otro.getMinutos()

        return retorno