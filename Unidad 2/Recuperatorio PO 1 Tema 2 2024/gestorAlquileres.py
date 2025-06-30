from claseAlquiler import Alquiler
import csv

class GestorAlquileres:
    __listaAlquileres: list

    def __init__(self):
        self.__listaAlquileres = []

    def agregarAlquiler(self, unAlquiler):
        self.__listaAlquileres.append(unAlquiler)

    def cargarAlquileres(self):
        archivo = open("Alquiler.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            self.agregarAlquiler(Alquiler(fila[0], fila[1], int(fila[2]), int(fila[3]), int(fila[4])))
        archivo.close()
    
    def ordenar(self):
        self.__listaAlquileres.sort(reverse=True)

    def listarAlquileres(self, GC):
        self.ordenar()
        totalImporte = 0
        print("Alquileres registrados:")
        print("Hora | Id de cancha | Duracion | Importe por hora | Importe alquiler")
        for alquiler in self.__listaAlquileres:
            idCancha = alquiler.getIdCancha()
            duracion = alquiler.getDuracion()
            duracion_horas = duracion // 60
            importePorHora = GC.obtenerImportePorHora(idCancha)
            print(f"{alquiler.getHora()}:{alquiler.getMinutos():02d} | {alquiler.getIdCancha()} | {duracion_horas} horas | ${importePorHora} | ${duracion_horas * importePorHora}")
            totalImporte += duracion_horas * importePorHora
        print(f"Importe total de alquileres: ${totalImporte}")

    def mostrarMinutosAlquilada(self, idC):
        minutos = 0
        encontrado = False

        for alquiler in self.__listaAlquileres:
            if idC.lower() == alquiler.getIdCancha().lower():
                encontrado = True
                minutos += alquiler.getDuracion()

        if not encontrado:
            print("No se encontro la cancha en los alquileres registrados.")
        else:
            print(f"Duracion total de alquiler de la cancha: {minutos} minutos")
    