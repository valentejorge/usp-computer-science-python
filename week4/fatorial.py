numero = int(input('Digite o valor de n: '))

subtração = numero - 1

if not numero == 0:
    while subtração != 0:
        numero = numero * (subtração)
        subtração -= 1
else:
    numero = 1
print(numero)
