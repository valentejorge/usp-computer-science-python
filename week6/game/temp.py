from funPartida import computador_escolhe_jogada
from funPartida import usuario_escolhe_jogada
from funPartida import partida

def capeonato():
    rodada = 1
    contador = 3
    print('você escolheu campeonato!')
    while contador != 0:
        print(f'\n**** rodada {rodada} ****\n')
        partida()
        rodada += 1
        contador -= 1
    print('**** final do campeonato! ****')
    print('placar: você 0 x 3 computador')
