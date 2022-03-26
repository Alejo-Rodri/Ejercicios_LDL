if __name__ == "__main__":
    print("Hola, vamos a ver cuanto te queda de tu sueldo libre.\n")

    viveres = int(input("Ingresa el costo de los viveres: "))
    agua = int(input("Ingresa el costo del recibo del agua: "))
    luz = int(input("Ingresa el costo del recibo de la luz: "))
    gas = int(input("Ingresa el costo del recibo del gas: "))
    internet = int(input("Ingresa el costo del internet: "))

    sueldo = int(input("Ingresa tu sueldo: "))
    sueldo_libre = sueldo - (viveres + agua + luz + gas + internet)

    if sueldo_libre < 0:
        print("Te hace falta plata, " + str(-sueldo_libre) + " pesos.")
    else:
        print("Te quedan " + str(sueldo_libre) + " pesos libres.")
