from claseGestorPlanes import GestorDePlanes, PlanTelefonia, PlanTelevision

def menu():
    op=None
    try:
        op=int(input("""
                                Menu de Opciones
                     [1] Mostrar que tipo de plan se encuentra almacenado en una posicion
                     [2] Mostrar cantidad de planes que corresponden a una cobertura geografica
                     [3] Ingresar una cantidad de canales internacionales para mostrar las compañias que ofrecen mayor o igual cantidad
                     [4] Mostrar detalles de los planes
                     [0] Salir
                     -> """))
    except ValueError:
        pass
    return op

if __name__=='__main__':
    GP = GestorDePlanes()
    GP.cargarPlanes()
    opcion = menu()

    while opcion != 0:
        if opcion == 1:
            try:
                pos = int(input("Indique la posicion: -> "))
                GP.mostrarTipoPlan_PorIndice(pos)
            except ValueError:
                print("Se esperaba un numero entero")
            except IndexError:
                print("Indice fuera de rango.")
        elif opcion == 2:
            cob = input("Ingrese la cobertura geografica: ->")
            GP.mostrarPlanes_PorCoberturaGeo(cob)
        elif opcion == 3:
            try:
                cant = int(input("Ingrese por teclado la cantidad de canales internacionales: ->"))
                GP.mostrarNombresComp(cant)
            except ValueError:
                print("Error. Se esperaba un numero entero")
        elif opcion == 4:
            GP.mostrarDetallesPlanes()
        else:
            print("Opcion invalida")
        opcion = menu()