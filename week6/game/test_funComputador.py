from funPartida import computador_escolhe_jogada

def test1_3():
    assert computador_escolhe_jogada(1, 3) == 1

def test3_2():
    assert computador_escolhe_jogada(2, 2) == 2
