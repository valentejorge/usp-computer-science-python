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
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    from string import punctuation

    def deleta_pontos(texto):
        for caracteres in punctuation:
            texto = texto.replace(caracteres, '')
        return(texto)

    def contar_letras(texto_separado):
        total = 0
        for palavras in texto_separado:
            for letras in palavras:
                total += 1
        return total
    
    def contar_frases(texto):
        frases_separadas = []
        for sentencas in separa_sentencas(texto):
            frases_separadas += separa_frases(sentencas)
        return len(frases_separadas)

    n_de_sentencas = len(separa_sentencas(texto))

    n_de_letras = contar_letras(texto)

    n_de_frases = contar_frases(texto)

    texto = deleta_pontos(texto)

    texto_separado = separa_palavras(texto)

    total_de_palavras = len(texto_separado)

    tam_medio_palavra = contar_letras(texto_separado) / total_de_palavras

    relacao_type_token = n_palavras_diferentes(texto_separado) / total_de_palavras

    razao_hapax_legonama = n_palavras_unicas(texto_separado) / total_de_palavras

    tam_medio_sentença = n_de_letras / n_de_sentencas

    complexidade_sentença = n_de_frases / n_de_sentencas

    tam_medio_frase = contar_letras(texto) / n_de_frases

    print('Tamanho Médio de Palavras: ', tam_medio_palavra)

    print('Relação Type-Token: ', relacao_type_token)

    print('Razão Hapax Legonama: ', razao_hapax_legonama)

    print('Tamanho Médio de Sentença: ', tam_medio_sentença)

    print('Complexidade de Sentença: ', complexidade_sentença)

    print('Tamanho Médio de frases:', tam_medio_frase)

    return(tam_medio_palavra, relacao_type_token, razao_hapax_legonama, tam_medio_sentença, complexidade_sentença, tam_medio_frase)

calcula_assinatura('o gato caçava o rato')

print()
print()
print()
calcula_assinatura('Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.')

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass
