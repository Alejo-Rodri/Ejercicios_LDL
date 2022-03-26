if __name__ == "__main__":
    seleccionador = 10
    costo_acum = 0

    print("Vamos a armar tu traje perfecto\n")

    costo_corbata = int(str(input("Ingresa el precio de la corbata: ")))
    costo_total = costo_corbata * 6
    costo_cinturon = costo_total * (1/5)
    costo_zapatos = costo_total * (1/2)
    costo_camisa = costo_total - (costo_corbata + costo_cinturon + costo_zapatos)  # si calculaba el costo de la camisa según el costo de los zapatos
    # no daba exacto el acumulador de los costos con el costo total, entonces por eso lo calcule de esta forma

    while seleccionador != 0:
        seleccionador = int(input("1.Seleccionar la corbata\n2.Seleccionar el cinturon\n3.Seleccionar los zapatos\n4.Seleccionar la "
              "camisa\n0.Salir\n"))
        if seleccionador == 1:
            costo_acum += costo_corbata
        elif seleccionador == 2:
            costo_acum += costo_cinturon
            print("El cinturon te costaria " + str(costo_cinturon) + " pesos")
        elif seleccionador == 3:
            costo_acum += costo_zapatos
            print("Los zapatos te costarian " + str(costo_zapatos) + " pesos")
        elif seleccionador == 4:
            costo_acum += costo_camisa
            print("La camisa te costaria " + str(costo_camisa) + " pesos")
        else:
            print("Por favor ingresa una opción correcta.")

    print("Con lo que compraste el traje te sale por: " + str(costo_acum))

