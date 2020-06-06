from funPartida import computador_escolhe_jogada
from funPartida import usuario_escolhe_jogada

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    #define quem vai executar a primeira jogada
    if n % (m + 1) == 0:
        print('\nVocê começa!')
        retirada = n
        while retirada == 0 or retirada > m or retirada < 0:
            retirada = usuario_escolhe_jogada(n, m)
            if retirada == 0 or retirada > m or retirada < 0:
                print('\n***Jogada Inválida!***')
        n -= retirada
        print(f'agora restam {n} peças no tabuleiro')
        vez = 'computador'
    else:
        print('\nComputador começa!')
        retirada = computador_escolhe_jogada(n, m)
        n -= retirada

        print(f'\no computador tirou {retirada} peças')
        print(f'agora restam {n} peças no tabuleiro')
        vez = 'usuario'

    while n != 0:
        if vez == 'computador':
            retirada = computador_escolhe_jogada(n, m)
            n -= retirada

            print(f'\no computador tirou {retirada} peças')
            if n != 0:
                print(f'agora restam {n} peças no tabuleiro')
            else:
                print('\nFim do Jogo! O computador ganhou!')

            vez = 'usuario'
        else:
            retirada = n
            while retirada == 0 or retirada > m or retirada < 0:
                retirada = usuario_escolhe_jogada(n, m)
                if retirada == 0 or retirada > m or retirada < 0:
                    print('\n***Jogada Inválida!***')
            n -= retirada
            print(f'agora restam {n} peças no tabuleiro')
            vez = 'computador'

partida()


#jogadas validas são:
    #n != 0
    #n <= m
    #not n < 0
