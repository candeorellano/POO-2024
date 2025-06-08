import csv
from clasePlanTelefonia import PlanTelefonia
from clasePlanTelevision import PlanTelevision
from claseNodo import NodoPlan

class GestorDePlanes: #lista definida por el programador
    __comienzo: NodoPlan
    
    def __init__(self):
        self.__comienzo=None

    def agregarPlan(self, unPlan):
        nodo = NodoPlan(unPlan)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
    
    def cargarPlanes(self):
        band = False
        archivo = open("planes.csv")
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            if band is False:
                band = True
            else:
                if fila[0] == 'M':
                    self.agregarPlan(PlanTelefonia(fila[1], int(fila[2]), fila[3], float(fila[4]), fila[5], int(fila[6])))
                else:
                    self.agregarPlan(PlanTelevision(fila[1], int(fila[2]), fila[3], float(fila[4]), int(fila[5]), int(fila[6])))
        archivo.close()

    def contar_nodos(self):
        aux = self.__comienzo
        cont = 0
        while aux is not None:
            cont += 1
            aux = aux.getSiguiente()
        return cont

    def mostrarTipoPlan_PorIndice(self, pos):
            aux = self.__comienzo
            indice = 0
            if (pos < 0) or (pos > self.contar_nodos()):
                raise IndexError
            
            while aux is not None:
                if indice == pos:
                    dato = aux.getDato()
                    if isinstance(dato, PlanTelefonia):
                            print("El plan es de tipo telefonia")
                    elif isinstance(dato, PlanTelevision):
                            print("El plan es de tipo television")
                aux = aux.getSiguiente()
                indice += 1

    def mostrarPlanes_PorCoberturaGeo(self, cob):
        cont=0
        aux = self.__comienzo
        while aux!=None:
            if aux.getDato().getCobertura() == cob:
                cont += 1
            aux = aux.getSiguiente()
        print(f"La cantidad de planes que corresponden a esa cobertura geografica es: {cont}")
    
    def mostrarNombresComp(self, cant):
        aux = self.__comienzo
        while aux is not None:
            dato = aux.getDato()
            if isinstance(dato, PlanTelevision):
                if dato.getCantCanalesInternacionales() >= cant:
                    print(f"Nombre de la compañia: {dato.getNombreCompania()}")
            aux = aux.getSiguiente()
        
    def mostrarDetallesPlanes(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()
    