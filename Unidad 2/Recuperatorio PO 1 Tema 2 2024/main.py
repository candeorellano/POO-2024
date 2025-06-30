from gestorAlquileres import GestorAlquileres
from gestorCanchas import GestorCanchas

def menu():
    op = int(input("""MENU DE OPCIONES:
                   [1] Listar alquileres registrados
                   [2] Mostrar cantidad de minutos que estuvo alquilada una cancha
                   [0] SALIR
                   Ingrese una opcion: """))
    return op

if __name__ == "__main__":
    gestorCanchas = GestorCanchas()
    gestorCanchas.cargarCanchas()
    
    gestorAlquileres = GestorAlquileres()
    gestorAlquileres.cargarAlquileres()
    
    opcion = menu()
    
    while opcion != 0:
        if opcion == 1:
            gestorAlquileres.listarAlquileres(gestorCanchas)
        elif opcion == 2:
            idCancha = input("Ingrese el ID de la cancha: ")
            gestorAlquileres.mostrarMinutosAlquilada(idCancha)
        else:
            print("Opción no válida. Intente nuevamente.")
        opcion = menu()
    print("Saliendo del programa...")  # Optional exit message