def fatorial(n):
    fat = n

    subtração = n - 1

    if not n == 0:
        while subtração != 0:
            n = n * (subtração)
            subtração -= 1
    else:
        n = 1
    print(n)
    return fat
