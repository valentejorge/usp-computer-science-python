import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):


    def separa_frases_de_sentencas(lista_de_sentencas):
        frases_separadas = []
        for sentenca in lista_de_sentencas:
            frases_separadas += separa_frases(sentenca)
        return frases_separadas

    def separa_palavras_de_frases(lista_de_frases):
        palavras_separadas = []
        for frases in lista_de_frases:
            palavras_separadas += separa_palavras(frases)
        return palavras_separadas

    def caracteres_totais(lista_de_palavras):
        total = 0
        for palavras in lista_de_palavras:
            for caracteres in palavras:
                total += 1
        return total

    def caracteres_sem_pontuacao(texto):
        from string import punctuation
        total = 0
        for letras in texto:
            total += 1
            if letras in punctuation:
                total -= 1
        return total

    texto_com_sentencas_separadas = separa_sentencas(texto)

    texto_com_frases_separadas = separa_frases_de_sentencas(texto_com_sentencas_separadas)

    texto_com_palavras_separadas = separa_palavras_de_frases(texto_com_frases_separadas)

    n_de_caracteres_sem_pontos_finais = caracteres_totais(texto_com_sentencas_separadas)

    n_de_caracteres_com_espaco_sem_ponto_nenhum = caracteres_sem_pontuacao(texto)

    n_de_palavras = len(texto_com_palavras_separadas)

    n_de_sentencas = len(texto_com_sentencas_separadas)

    n_de_frases = len(texto_com_frases_separadas)

    n_de_caracteres = caracteres_totais(texto_com_palavras_separadas)

    total_de_palavras_diferente = n_palavras_diferentes(texto_com_palavras_separadas)

    total_de_palavras_unicas = n_palavras_unicas(texto_com_palavras_separadas)

    def tam_medio_palavra(caracteres, n_de_palavras):
        resultado = caracteres / n_de_palavras 
        return resultado

    print('tamanho_medio_palavras: ', end='')
    print(tam_medio_palavra(n_de_caracteres, n_de_palavras))

    def relacao_type_token(n_de_palavras_diferente, n_de_palavras):
        resultado = n_de_palavras_diferente / n_de_palavras
        return resultado

    def razao_hapax_legonama(total_de_palavras_unicas, n_de_palavras):
        resultado = total_de_palavras_unicas / n_de_palavras
        return resultado


    def tam_medio_sentenca(n_de_caracteres, n_de_sentencas):
        resultado = n_de_caracteres / n_de_sentencas
        return resultado


    def complexidade_de_sentenca(n_de_frases, n_de_sentencas):
        resultado = n_de_frases / n_de_sentencas
        return resultado


    def tamanho_medio_de_frase(n_de_caracteres_com_espaco_sem_ponto_nenhum, n_de_frases):
        resultado = n_de_caracteres_com_espaco_sem_ponto_nenhum / n_de_frases
        return resultado

    # print('relacao_type_token: ', end='')
    # print(relacao_type_token(total_de_palavras_diferente, n_de_palavras))

    # print('razao_hapax_legonama: ', end='')
    # print(razao_hapax_legonama(total_de_palavras_unicas, n_de_palavras))

    # print('tam_medio_sentenca: ', end='')
    # print(tam_medio_sentenca(n_de_caracteres_sem_pontos_finais, n_de_sentencas))

    # print('complexidade_de_sentenca: ', end='')
    # print(complexidade_de_sentenca(n_de_frases, n_de_sentencas))

    # print('tamanho_medio_de_frase: ', end='')
    # print(tamanho_medio_de_frase(n_de_caracteres_com_espaco_sem_ponto_nenhum, n_de_frases))

    a0 = tam_medio_palavra(n_de_caracteres, n_de_palavras)
    a1 = relacao_type_token(total_de_palavras_diferente, n_de_palavras)
    a2 = razao_hapax_legonama(total_de_palavras_unicas, n_de_palavras)
    a3 = tam_medio_sentenca(n_de_caracteres_sem_pontos_finais, n_de_sentencas)
    a4 = complexidade_de_sentenca(n_de_frases, n_de_sentencas)
    a5 = tamanho_medio_de_frase(n_de_caracteres_com_espaco_sem_ponto_nenhum, n_de_frases)

    return [a0, a1, a2, a3, a4, a5]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass








# def testa_calcula_assinatura(texto, valor_esperado):
    # valor_calculdado = calcula_assinatura(texto)
    # if valor_calculdado != valor_esperado:
        # print('Erro')
        # print('Valor Calculado: ', valor_calculdado, 'valor_esperado', valor_esperado)
    # else:
        # print('Passou')


# testa_calcula_assinatura('Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.', [4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5])

