largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
resetaLargura = largura

while altura > 0:
    while largura > 1:
        print('', end='#')
        largura -= 1
    print('#')
    altura -= 1
    largura = resetaLargura
