from funcMaximo import maximo

def teste_0_1():
    assert maximo(0, 1) == 1

def test_10_0():
    assert maximo(10, 0) == 10

def test_negative():
    assert maximo(-10, 10) == 10
