ponto1x = float(input('Qual o x do ponto 1? '))
ponto2x = float(input('Qual o x do ponto 2? '))
ponto1y = float(input('Qual o y do ponto 1? '))
ponto2y = float(input('Qual o y do ponto 2? '))
distancia = (((ponto1x - ponto2x)**2) + ((ponto1y - ponto2y)**2))**0.5
if distancia >= 10:
    print ('longe')
elif distancia < 10:
    print ('perto')
