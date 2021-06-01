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
            print(retiro, "Retirados correctamente")


def consultar():
    print("Su dinero es de " + str(dinero))


def agregar():

    global dinero
    dinero1 = int(input("Digite el monto a agregar"))
    print("Se ha agregado correctamente el monto!!")
    dinero+= dinero1


while opcion != -1:
    opcion = int(input("Digite...\n(1) Para retirar dinero\n(2) Para consultar Cuenta\n(3) Para agregar Dinero\n(4) "
                       "Salir\n"))

    if opcion == 1:
        retirar(dinero)
    elif opcion == 2:
        consultar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        opcion = -1
    else:
        print("Numero incorrecto!!")

