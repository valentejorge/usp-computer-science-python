def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial *= n
        n -= 1
    return fatorial

n = 1
while n >= 0:
    n = int(input('digita caralho: '))
    print(fatorial(n))
