n = int(input('Digite um número n: '))

soma = 0
repetição = len(str(n))
resultado = 0

while repetição != 0:
    soma = n % 10
    n = n // 10
    resultado += soma
    repetição -= 1

print(resultado)
