from funcFatorial import fatorial

n = int(input('Qual o valor de n? '))
k = int(input('Qual o valor de k? '))

equals = (fatorial(n)) / (fatorial(k) * fatorial(n - k))

print(equals)
