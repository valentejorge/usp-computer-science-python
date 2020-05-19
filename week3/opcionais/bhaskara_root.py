valorA = float(input('Qual o valor de a? '))
valorB = float(input('Qual o valor de b? '))
valorC = float(input('Qual o valor de c? '))

Delta = valorB**2 - 4 * valorA * valorC

bask1 = ((-valorB) + (Delta**0.5)) / (2 * valorA)
bask2 = ((-valorB) - (Delta**0.5)) / (2 * valorA)

if Delta == 0:
    print (f'a raiz desta equação é {bask1}')
else:
    if Delta < 0:
        print (f'esta equação não possui raízes reais')
    else:
        if bask1 < bask2:
            print (f'as raízes da equação são {bask1} e {bask2}')
        else:
            print (f'as raízes da equação são {bask2} e {bask1}')
