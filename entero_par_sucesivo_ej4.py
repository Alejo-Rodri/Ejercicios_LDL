import funciones

if __name__ == "__main__":
    numero = int(input("Hola,\nIngresa un número entero: "))

    acum_num = numero
    acum_num_suc = 0
    i = 1
    while acum_num_suc != 3:
        if funciones.par_impar(numero + i):
            acum_num_suc += 1
            acum_num += numero + i
            print("El número " + str(acum_num_suc) + " par sucesivo es: " + str(numero + i))
        i += 1

    print("La suma de los números es: " + str(acum_num))
    print("La multiplicación de los números sumados por el número ingresado da: " + str(acum_num * numero))
