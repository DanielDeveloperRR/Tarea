# Cajero automatico
opcion = 0
dinero = 100


def retirar(plata=None):
    global dinero
    if plata == 0:
        print("Agregue dinero primero")
    else:
        retiro = int(input("Digite el dinero que desea retirar:\n"))
        if plata - retiro < 0:
            print("Fondos insuficientes")
        else:
            dinero = dinero - retiro
            print(dinero)


while opcion != -1:
    option = int(input("Digite...\n(1) Para retirar dinero\n(2) Para consultar Cuenta\n(3) Para agregar Dinero\n(4) "
                       "Salir\n"))

    if option == 1:
        retirar(dinero)
    elif option == 2:
        print("2")
    elif option == 3:
        print("3")
    elif option == 4:
        option = -1
    else:
        print("Numero incorrecto!!")
