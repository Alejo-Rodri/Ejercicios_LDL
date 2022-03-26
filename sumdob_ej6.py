if __name__ == "__main__":
    print("Hola vas a ingresar 3 números 10 veces,")
    for i in range(1, 11):
        num1 = int(input("Vas en el número " + str(i) + "\n" + "Ingresa el"
                         " número 1 por favor: "))
        num2 = int(input("Ingresa el número 2 por favor: "))
        num3 = int(input("Ingresa el número 3 por favor: "))

        suma = (num1 * 2) + (num2 * 3) - (num3 / 2)
        print("El resultado de la suma del doble del primer número con el triple "
              " del segundo menos la mitad del tercero es: " + str(suma))
