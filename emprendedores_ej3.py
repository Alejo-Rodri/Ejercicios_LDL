if __name__ == "__main__":
    camisas = [0, 0, 0, 0]
    pantalones = [0, 0, 0]
    zapatos = [0, 0]
    libros = [0, 0, 0, 0]

    acum_cam = 0
    acum_pan = 0
    acum_zap = 0
    acum_lib = 0

    print("Hola, esto va a calcular cuanto gastaste tú y tus amigos en el atuendo y libros")
    print("inferimos que todos compraron lo mismo u.u")

    for i in camisas:
        camisas[pantalones[0]] = int(input("Ingresa el valor de la camisa " + str(pantalones[0] + 1) + "\n"))  # me dio pereza declarar una variable separada como contador
        acum_cam += camisas[pantalones[0]]
        # entonces voy a usar los arrays como contadores
        pantalones[0] += 1  # los cuales también iré incrementando, después esos valores se borraran

    for i in pantalones:
        pantalones[zapatos[0]] = int(input("Ingresa el valor del pantalon " + str(zapatos[0] + 1) + "\n"))
        acum_pan += pantalones[zapatos[0]]
        zapatos[0] += 1

    for i in zapatos:
        zapatos[libros[0]] = int(input("Ingresa el valor del par de zapatos " + str(libros[0] + 1) + "\n"))
        acum_zap += zapatos[libros[0]]
        libros[0] += 1

    j = 0  # aquí si tuve que usar otra variable XD
    for i in libros:
        libros[j] = int(input("Ingresa el valor del libro " + str(j + 1) + "\n"))
        acum_lib += libros[j]
        j += 1

    total_atuendo = acum_cam + acum_pan + acum_zap

    personas = input("¿Con cuántas personas compraste esto, incluyendote? ")

    print("cada una de las " + personas + " personas que fueron de compras individualmente gastaron " + str(total_atuendo) + " pesos en el atuendo.")
    print("En libros se gastaron " + str(acum_lib) + " pesos.")
