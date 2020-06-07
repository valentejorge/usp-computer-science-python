from temp2 import computador_escolhe_jogada
from temp3 import usuario_escolhe_jogada

def test1_3():
    assert computador_escolhe_jogada(1, 3) == 1

def test3_2():
    assert computador_escolhe_jogada(2, 2) == 2

def test2_3():
    assert computador_escolhe_jogada(2, 3) == 2

def test3_3():
    assert computador_escolhe_jogada(3, 3) == 3
