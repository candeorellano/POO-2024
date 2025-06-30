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
        return (self.getIdJugador() == otro.getIdJugador() and
                self.getDireccionIP() != otro.getDireccionIP() and
                self.getFecha() == otro.getFecha() and
                self.getHoraInicio() == otro.getHoraInicio())

    def __lt__(self, otro):
        retorno = None

        if self.getIdJugador() != otro.getIdJugador():
            retorno = self.getIdJugador() < otro.getIdJugador()
        elif self.getFecha() != otro.getFecha():
            retorno = self.getFecha() < otro.getFecha()
        elif self.getHoraInicio() != otro.getHoraInicio():
            retorno = self.getHoraInicio() < otro.getHoraInicio()
        else:
            retorno = self.getDireccionIP() < otro.getDireccionIP()
        
        return retorno
