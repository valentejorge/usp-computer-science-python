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
        while computador_retirou >= m and not computador_retirou % (m + 1) == 0:
            computador_retirou -= 1
        computador_return = n - computador_retirou

    if computador_return == 0:
        computador_return = 1

    return computador_return
