def primo(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True


limite = int(input("Limite de primos: "))

n = 2
while n < limite:
    if primo(n):
        print(n, end=", ")
    n += 1
