import funciones

if __name__ == "__main__":
    numeros = []
    seleccionador = 1

    print("Hola, este programa juega con números que ingreses :D")

    while seleccionador != 0:
        seleccionador = int(input("¿Qué deseas hacer?\n0.Salir y enseñar los resultados\n1.Ingresar números entre -1000~1000\n"))
        if seleccionador == 0:
            if len(numeros) == 0:
                print("\tNo ingresaste ningún valor UnU")
                seleccionador = 0
            else:
                acum_par = 0
                acum_impar = 1
                pot_impar = []
                acum_negativos = 0
                j = 0

                for i in numeros:
                    if funciones.par_impar(i):
                        acum_par += numeros[j]
                        print("El número " + str(numeros[j]) + " es par.")
                    if not funciones.par_impar(i):
                        acum_impar = acum_impar * numeros[j]
                        print("El número " + str(numeros[j]) + " es impar.")
                    if not funciones.par_impar(i):
                        pot_impar.append(i ** 2)
                        print("La potencia par de " + str(i) + " es: " + str(i ** 2))
                    if numeros[j] < 0:
                        acum_negativos += numeros[j]
                        print("El número " + str(numeros[j]) + " es negativo.")
                    j += 1

                print("\n\nLa suma de los pares es: " + str(acum_par))
                print("El producto de los números impares es: " + str(acum_impar))
                print("La potencia par de los impares es: " + str(pot_impar))
                print("La suma de los negativos es: " + str(acum_negativos))

        elif seleccionador == 1:
            num_adj = int(input("Ingresa un número: "))
            if num_adj < -1000 or num_adj > 2000:
                print("\tEl número ingresado no está en el rango :/")
            else:
                numeros.append(num_adj)
                print(numeros)
        else:
            print("\tPor favor ingresa una opción correcta :(")

    print("Adiós.")
    