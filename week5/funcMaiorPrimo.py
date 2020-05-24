def primo(numero):

    if numero == 2 or numero == 3 or numero == 5 or numero == 7:
        return ('primo')
    elif numero == 1:
        return ('não primo')
    else:
        if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
            return ('não primo')
        else:
            return ('primo')
