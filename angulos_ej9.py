if __name__ == "__main__":
    ANGULO_RECTO = 90
    seleccionador = 1

    while seleccionador != 2:
        if seleccionador == 1:
            angulo_dado = int(input("Por favor ingresa la medida de un ángulo: "))
            print("La medida del tercer ángulo es: " + str(180 - (ANGULO_RECTO + angulo_dado)) + " grados.")
            seleccionador = int(input("¿Quieres seguir calculando el valor del tercer ángulo?\n1.SI\n2.NO\n"))

    print("Adiós uwu")
