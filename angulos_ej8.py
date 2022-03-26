if __name__ == "__main__":
    angulo_dado = int(input("Por favor ingresa la medida de un ángulo: "))

    if angulo_dado < 90:
        angulo_comp = 90 - angulo_dado
        print("El complemento del ángulo dado es otro ángulo de: " + str(angulo_comp) + " grados.")
        print("La suma de ambos es: " + str(angulo_dado + angulo_comp) + " grados.")
    elif 90 <= angulo_dado < 180:
        angulo_supl = 180 - angulo_dado
        print("El suplemento del ángulo dado es otro ángulo de: " + str(angulo_supl) + " grados.")
        print("La suma de ambos es: " + str(angulo_dado + angulo_supl) + " grados.")
    else:
        print("Ingresa un ángulo correcto")
