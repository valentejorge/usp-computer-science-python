n = int(input('Digite o valor de n: '))

repetição = n * 2
impar = 0

while repetição != 0:
    impar += 1
    if not impar % 2 == 0:
        print(impar)
    repetição -= 1
