if __name__ == "__main__":
    acum_notas = 0

    print("""Por favor ingrese las notas en este formato
    10, 20, 30, 40, 50""")

    for i in range(1, 7):
        acum_notas += int(input("Ingrese cuanto sacó en la nota " + str(i) + "\n"))

    promedio = acum_notas / 6

    if promedio > 35:
        print("El promedio es " + str(promedio) + " ha aprobado el semestre")
    else:
        print("El promedio es " + str(promedio) + "ha reprobado")
