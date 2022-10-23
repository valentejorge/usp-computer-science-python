lista = []

numb = 1

while numb != 0:
    numb = int(input("Digite um número: "))
    lista.append(numb)

del(lista[-1])

for x in reversed(lista):
    print(x)
