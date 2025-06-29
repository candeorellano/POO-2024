from claseGammer import Gammer
import csv

class GestorGamers:
    __listaGammers: list

    def __init__(self):
        self.__listaGammers = []

    def agregarGammer(self, unGammer):
        self.__listaGammers.append(unGammer)

    def cargarArchivo(self):
        archivo = open("gammers.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:
            self.agregarGammer(Gammer(int(fila[0]), int(fila[1]), fila[2], fila[3], fila[4], fila[5], int(fila[6]), int(fila[7])))
        archivo.close()
    
    def buscarGammerPorDNI(self, dni):
        i = 0
        encontrado = False

        while i < len(self.__listaGammers) and not encontrado:
           if self.__listaGammers[i].getDni() == dni:
               encontrado = True
           else:
               i += 1
        
        return encontrado
    
    def listarConexionesPorDNI(self, dni, gestorConexiones):
        i = 0
        encontrado = False

        while i < len(self.__listaGammers) and not encontrado:
           if self.__listaGammers[i].getDni() == dni:
               encontrado = True
           else:
               i += 1
        
        if encontrado:
            id = self.__listaGammers[i].getId()
            nombre = self.__listaGammers[i].getNombre()
            apellido = self.__listaGammers[i].getApellido()
            alias = self.__listaGammers[i].getAlias()
            plan = self.__listaGammers[i].getPlan()
            importeBase = self.__listaGammers[i].getImporteBase()

            print(f"""
            DNI: {dni}  Nombre y Apellido: {nombre} {apellido}
            Alias: {alias}  Plan: {plan}  Importe Base: {importeBase}""")
            horasJuego = gestorConexiones.mostrarConexionesPorId(id)
            tiempoLimite = self.__listaGammers[i].getTiempoLimite()
            exceso = horasJuego - tiempoLimite
            if exceso < 0: # Si el exceso es negativo, significa que no hay horas en exceso
                exceso = 0
            print(f"""
            Total de horas:{horasJuego}     Horas en exceso:{exceso}""")
            importe = horasJuego * importeBase
            if exceso > 0:
                if plan == "Basico":
                    importe += exceso * (importeBase * 0.25)
                elif plan == "Completo":
                    importe += exceso * (importeBase * 0.30)
                else:
                    importe += exceso * (importeBase * 0.40)
            print(f"Importe a facturar: {importe}")
        else:
            print("No se encontro jugador con el DNI ingresado.")

    def mostrarGammerPorId(self, id):
        encontrado = False
        i = 0

        while i < len(self.__listaGammers) and not encontrado:
            if self.__listaGammers[i].getId() == id:
                encontrado = True
            else:
                i += 1
        
        if encontrado:
            nom = self.__listaGammers[i].getNombre()
            ape = self.__listaGammers[i].getApellido()
            alias = self.__listaGammers[i].getAlias()
            plan = self.__listaGammers[i].getPlan()
            print(f"Nombre: {nom}  Apellido: {ape}  Alias: {alias}  Plan: {plan}")
        else:
            print(f"No se encontro jugador con ID: {id}")

    def mostrarJugadoresBasicoSimultaneo(self, GC):
        GC.ordenar()
        print("Jugadores con plan Basico que se conectan en IPs distintas simultaneamente:")
        for gammer in self.__listaGammers:
            if gammer.getPlan() == "Basico":
                if GC.listadoBasicos(gammer.getId()):
                    print(f"Nombre: {gammer.getNombre()}  Apellido: {gammer.getApellido()}")