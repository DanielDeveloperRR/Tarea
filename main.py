# Cajero automatico
option = 0
while option != -1:
    option = int(input("Digite...\n(1) Para retirar dinero\n(2) Para consultar Cuenta\n(3) Para agregar Dinero\n(4) "
                       "Salir\n"))

    if option == 1:
        print("1")
    elif option == 2:
        print("2")
    elif option == 3:
        print("3")
    elif option == 4:
        option = -1
    else:
        print("Numero incorrecto!!")


def control1():
    print("pagina1")


control1()
