def inicio():
    print('Bem vindo ao jogo do NIM! Escolha:\n')
    modo_de_jogo = int(
        input(
            '1 - para jogar uma partida isolada\n2 - para jogar um campeonato '
        ))
    if modo_de_jogo == 1:
        print('\nvocê escolheu uma partida isolada!\n')
        partida()
    else:
        campeonato()


def campeonato():
    rodada = 1
    contador = 3
    print('\nvocê escolheu campeonato!')
    #repete 3 vezes o titulo mostrando em qual rodada você está
    while contador != 0:
        print(f'\n**** Rodada {rodada} ****\n')
        partida()
        rodada += 1
        contador -= 1
    print('\n**** final do campeonato! ****')
    print('\nplacar: você 0 x 3 computador')


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    #define quem vai executar a primeira jogada
    if n % (m + 1) == 0:
        print('\nVocê começa!')
        retirada = usuario_escolhe_jogada(n, m)
        n -= retirada
        print(f'agora restam {n} peças no tabuleiro')
        vez = 'computador'

    else:
        print('\nComputador começa!')
        retirada = computador_escolhe_jogada(n, m)
        n -= retirada
        print(f'\no computador tirou {retirada} peças')
        print(f'agora restam {n} peças no tabuleiro')

        if n == 0:
            print('\nFim do Jogo! O computador ganhou!')

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
            retirada = usuario_escolhe_jogada(n, m)
            n -= retirada
            print(f'agora restam {n} peças no tabuleiro')

            vez = 'computador'


def computador_escolhe_jogada(n, m):
    computador_retirou = n
    if computador_retirou == m:
        computador_return = m
    elif computador_retirou < m:
        computador_return = computador_retirou
    #essa aqui ta dando erro
    elif computador_retirou % (m + 1) == 0:
        computador_retirou = m
        computador_return = computador_retirou
    else:
        while computador_retirou >= m and not computador_retirou % (
                m + 1) == 0:
            computador_retirou -= 1
        computador_return = n - computador_retirou

    if computador_return == 0:
        computador_return = 1

    return computador_return


def usuario_escolhe_jogada(n, m):
    jogador_retirou = int(input('\nQuantas peças você vai tirar? '))
    while jogador_retirou > m or jogador_retirou <= 0:
        print('\nOops! Jogada inválida! Tente de novo.')
        jogador_retirou = int(input('\nQuantas peças você vai tirar? '))
    return jogador_retirou


inicio()
