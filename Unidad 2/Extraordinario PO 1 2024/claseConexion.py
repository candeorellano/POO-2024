class Conexion:
    __idJugador:int
    __direccionIP:str
    __juego:str
    __fecha:str
    __horaInicio:int
    __horaFin:int

    def __init__(self, idJugador, direccionIP, juego, fecha, horaInicio, horaFin):
        self.__idJugador = idJugador
        self.__direccionIP = direccionIP
        self.__juego = juego
        self.__fecha = fecha
        self.__horaInicio = horaInicio
        self.__horaFin = horaFin

    def getIdJugador(self):
        return self.__idJugador
    
    def getDireccionIP(self):
        return self.__direccionIP
    
    def getJuego(self):
        return self.__juego
    
    def getFecha(self):
        return self.__fecha
    
    def getHoraInicio(self):
        return self.__horaInicio
    
    def getHoraFin(self):
        return self.__horaFin
    
    def __str__(self):
        return f"ID Jugador: {self.__idJugador}, Direccion IP: {self.__direccionIP}, Juego: {self.__juego}, Fecha: {self.__fecha}, Hora Inicio: {self.__horaInicio}, Hora Fin: {self.__horaFin}"
    
    def __eq__(self, otro):
        return (self.__idJugador == otro.getIdJugador() and
                self.__direccionIP != otro.getDireccionIP() and
                self.__fecha == otro.getFecha() and
                self.__horaInicio == otro.getHoraInicio())

    def __lt__(self, otro):
        retorno = None

        if self.__idJugador != otro.getIdJugador():
            retorno = self.__idJugador < otro.getIdJugador()
        elif self.__fecha != otro.getFecha():
            retorno = self.__fecha < otro.getFecha()
        elif self.__horaInicio != otro.getHoraInicio():
            retorno = self.__horaInicio < otro.getHoraInicio()
        else:
            retorno = self.__direccionIP < otro.getDireccionIP()
        
        return retorno
