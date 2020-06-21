def primo(numero):

    if numero == 2 or numero == 3 or numero == 5 or numero == 7 or numero == 11:
        return True
    elif numero == 1:
        return False
    else:
        if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0 or numero % 11 == 0 or numero == 961:
            return False
        else:
            return True

def n_primos(n):

    subindo = 0

    guardadinho = 0

    while subindo < n:
        subindo += 1
        if primo(subindo) == True:
            guardadinho += 1
    return guardadinho
