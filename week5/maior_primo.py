from primo import ehprimo

def maior_primo(entrada):

    subindo = 0

    guardadinho = 0

    while subindo < entrada:
        subindo += 1
        if ehprimo(subindo) == True:
            guardadinho = subindo
    return guardadinho
