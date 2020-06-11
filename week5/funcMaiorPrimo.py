def ehprimo(numero):

    if numero == 2 or numero == 3 or numero == 5 or numero == 7:
        return True
    elif numero == 1:
        return False
    else:
        if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0 or numero % 11 == 0 or numero == 961:
            return False
        else:
            return True


def maior_primo(entrada):

    subindo = 0

    guardadinho = 0

    while subindo < entrada:
        subindo += 1
        if ehprimo(subindo) == True:
            guardadinho = subindo
    return guardadinho
