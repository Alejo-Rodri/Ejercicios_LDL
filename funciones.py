def par_impar(numero):  # esta función calcula si un número es par o impar
    if numero % 2 == 0:  # regresa True o False
        return True
    else:
        return False


def primalidad(numero):  # esta función calcula si un número es primo
    if numero == 0:  #
        return False
    elif numero == 1:
        return False

    for i in range(2, numero+1):
        if numero % i == 0:
            if numero == i:
                return True
            else:
                return False


def factorial(numero):
    acum_factorial = 1
    for i in range(2, numero+1):
        acum_factorial = acum_factorial * i

    return acum_factorial
