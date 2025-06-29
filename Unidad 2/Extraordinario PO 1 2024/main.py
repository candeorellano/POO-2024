from gestorGammers import GestorGamers
from gestorConexiones import GestorConexiones

def menu():
    op = int(input("""MENU DE OPCIONES:
                [1] Mostrar listado de conexiones de un gammer
                [2] Mostrar datos de jugadores que jugaron un juego
                [3] Listar jugadores que tienen plan Basico, que se conectan en IPs distitnas simultaneamente
                [0] Salir
                Indique su opcion: """))
    
    return op

if __name__=='__main__':
    gestorGammers = GestorGamers()
    gestorConexiones = GestorConexiones()
    
    gestorGammers.cargarArchivo()
    gestorConexiones.cargarArchivo()
    
    opcion = menu()
    
    while opcion != 0:
        if opcion == 1:
            dni = int(input("Ingrese el DNI del jugador: "))
            gestorGammers.listarConexionesPorDNI(dni, gestorConexiones)
        elif opcion == 2:
            juego = input("Ingrese el nombre del juego: ")
            gestorConexiones.mostrarJugadoresPorJuego(juego, gestorGammers)
        elif opcion == 3:
            gestorGammers.mostrarJugadoresBasicoSimultaneo(gestorConexiones)
        else:
            print("Opcion no valida. Intente nuevamente.")
        opcion = menu()
    print("Saliendo del programa...")