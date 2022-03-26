if __name__ == "__main__":
    acum_apro = 0
    acum_repro = 0

    cant_est = int(input("Ingrese la cantidad de estudiantes con los que se va a trabajar.\n"))
    print("""Por favor ingrese las notas en este formato
                10, 20, 30, 40, 50""")
    for i in range(1, cant_est+1):
        print("Para el estudiante número " + str(i))
        acum_notas = 0

        for i in range(1, 7):
            acum_notas += int(input("Ingrese cuanto sacó en la nota " + str(i) + "\n"))

        promedio = acum_notas / 6

        if promedio > 35:
            print("El promedio es " + str(promedio) + " ha aprobado el semestre.")
            acum_apro += 1
        else:
            print("El promedio es " + str(promedio) + " ha reprobado el semestre.")
            acum_repro += 1

    print(str(acum_apro) + " estudiantes aprobaron el semestre y " + str(acum_repro) + " reprobaron el semestre.")
