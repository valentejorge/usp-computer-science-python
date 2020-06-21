largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

contador = largura

while altura > 1:
    if contador < largura and contador > 0:
        print('#', (largura - 3) * ' ', end='')
    elif contador == largura:
        print((largura - 1) * '#', end='')
    print('#')
    altura -= 1
    contador -= 1

print((largura) * '#', end='')
