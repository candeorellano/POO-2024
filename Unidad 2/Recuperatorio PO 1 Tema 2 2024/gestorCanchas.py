from claseCancha import Cancha
import csv
import numpy as np

class GestorCanchas:
    __dimension:int
    __cantidad:int
    __incremento:int
    __listaCanchas:np.ndarray

    def __init__(self):
        self.__dimension = 3
        self.__cantidad = 0
        self.__incremento = 3
        self.__listaCanchas = np.empty(self.__dimension, dtype=Cancha)

    def agregarCancha(self, unaCancha):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaCanchas.resize(self.__dimension)
        self.__listaCanchas[self.__cantidad] = unaCancha
        self.__cantidad += 1
    
    def cargarCanchas(self):
        archivo = open("Canchas.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)  # Skip header
        for fila in reader:
            self.agregarCancha(Cancha(fila[0], fila[1], int(fila[2])))
        archivo.close()

    def obtenerImportePorHora(self, idCancha):
        i = 0
        encontrado = False
        importeHora = 0
        while i < self.__cantidad and not encontrado:
            if self.__listaCanchas[i].getId() == idCancha:
                encontrado = True
                importeHora = self.__listaCanchas[i].getImportePorHora()
            else:
                i += 1
        
        return importeHora
