def usuario_escolhe_jogada(n, m):
    jogador_retirou = int(input('\nQuantas peças você vai tirar? '))
    while jogador_retirou > m or jogador_retirou <= 0:
        print('Oops! Jogada inválida! Tente de novo.')
        jogador_retirou = int(input('\nQuantas peças você vai tirar? '))
    return jogador_retirou



def usuario_escolhe_jogada(n, m):
    jogador_retirou = int(input('\nQuantas peças você vai tirar? '))
    return jogador_retirou
