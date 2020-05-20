number = int(input('Digite um número inteiro: '))

t = len(str(number))
tamanho = len(str(number))
sim = 'null'
não = 'null'

while tamanho != 0:
    comparação = number % 10
    number = number // 10
    tamanho -= 1
    if comparação == number % 10:
        sim = 'sim'
    else:
        não = 'não'
if (não == 'não' and sim == 'null') or (t == 1):
    print ('não')
elif sim == 'sim':
    print ('sim')
