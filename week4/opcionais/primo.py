numero = int(input('Digite um número inteiro: '))

if numero == 2 or numero == 3 or numero == 5 or numero == 7:
    print ('primo')
elif numero == 1:
    print ('não primo')
else:
    if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        print ('não primo')
    else:
        print ('primo')
