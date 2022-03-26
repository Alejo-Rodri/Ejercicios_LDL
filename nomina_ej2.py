if __name__ == "__main__":
    horas_extra = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    total_nomina = 0
    j = 0

    # si trabaja entre 10 a 20 horas obtendrá una bonificación del 10%
    # si trabaja entre 20 a 32 horas obtendrá una bonificación del 15%
    # si trabaja más de 32 horas obtendrá un 20% de bonificación

    for i in horas_extra[0]:
        horas_extra[0][j] = int(input("Cuantas horas extra trabajó el empleado " + str(j + 1) + "\n"))

        if 10 < horas_extra[0][j] < 20:
            horas_extra[1][j] += (855000 + (855000 * 0.1)) - (855000 * 0.26)
            total_nomina += horas_extra[1][j]
        elif 20 < horas_extra[0][j] < 32:
            horas_extra[1][j] += (855000 + (855000 * 0.15)) - (855000 * 0.26)
            total_nomina += horas_extra[1][j]
        elif horas_extra[0][j] > 32:
            horas_extra[1][j] += (855000 + (855000 * 0.2)) - (855000 * 0.26)
            total_nomina += horas_extra[1][j]
        else:
            horas_extra[1][j] += 855000 - (855000 * 0.26)
            total_nomina += horas_extra[1][j]

        j += 1

    print(horas_extra)
    print("La nomina total que debe pagar el dueño de la empresa es de " + str(total_nomina) + " pesos.")
