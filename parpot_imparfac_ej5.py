import funciones

if __name__ == "__main__":
    numero = int(input("Bienvenido,\nPor favor ingruesa un número entero: "))

    if funciones.par_impar(numero):
        print("El número " + str(numero) + " elevado a la potencia 7 da: " + str(numero ** 7))
    else:
        print("El factorial del número " + str(numero) + " da: " + str(funciones.factorial(numero)))
