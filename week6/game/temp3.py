def usuario_escolhe_jogada(n, m):
    nCache = n
    nCache = int(input('\nQuantas peças você vai tirar? '))
    if nCache > m:
        jogador_retirou = int(input('\nQuantas peças você vai tirar? '))
    return jogador_retirou
