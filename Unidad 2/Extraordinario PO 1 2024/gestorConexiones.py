from claseConexion import Conexion
import csv
import numpy as np

class GestorConexiones:
    __dimension:int
    __cantidad:int
    __incremento:int
    __listaConexiones: np.ndarray

    def __init__(self):
        self.__dimension = 10
        self.__cantidad = 0
        self.__incremento = 8
        self.__listaConexiones = np.empty(self.__dimension, dtype=Conexion)

    def agregarConexion(self, unaConexion):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaConexiones.resize(self.__dimension)
        self.__listaConexiones[self.__cantidad] = unaConexion
        self.__cantidad += 1

    def cargarArchivo(self):
        archivo = open("conexiones.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:
            self.agregarConexion(Conexion(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5])))
        archivo.close()

    def mostrarConexionesPorId(self, id):
        acumHoras = 0
        print("""
        IP de conexion | Juego | Fecha | Hora Inicio | Hora Fin""")
        for i in range(self.__cantidad):
            conexion = self.__listaConexiones[i]
            if conexion.getIdJugador() == id:
                print(f"""
                {conexion.getDireccionIP()} | {conexion.getJuego()} | {conexion.getFecha()} | {conexion.getHoraInicio()} | {conexion.getHoraFin()}""")
                horasJuego = conexion.getHoraFin() - conexion.getHoraInicio()
                acumHoras += horasJuego
        return acumHoras
    
    def mostrarJugadoresPorJuego(self, juego, GG):
        encontrado = False

        print(f"Jugadores que jugaron '{juego}':")
        for i in range(self.__cantidad):
            conexion = self.__listaConexiones[i]
            if conexion.getJuego().lower() == juego.lower():
                encontrado = True
                ip = conexion.getDireccionIP()
                id = conexion.getIdJugador()
                print(f"IP: {ip} | ID Jugador: {id}")
                GG.mostrarGammerPorId(id)
    
        if not encontrado:
            print(f"No se encontro el juego '{juego}' en las conexiones.")

    def ordenar(self):
        self.__listaConexiones.sort()

    def listadoBasicos(self, id):
        bandera = False
        i = 0

        for i in range(self.__cantidad):
            conexionA = self.__listaConexiones[i]
            if conexionA.getIdJugador() == id:
                for j in range(self.__cantidad):
                    if i != j:
                        conexionB = self.__listaConexiones[j]
                        if conexionB.getIdJugador() == id and conexionA == conexionB:
                                bandera = True

        return bandera
