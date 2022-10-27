import re
from similaridade import n_palavras_unicas
from similaridade import n_palavras_diferentes
from similaridade import separa_palavras
from string import punctuation
from similaridade import separa_sentencas
from similaridade import separa_frases

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def calcula_assinatura(texto):
    texto_separado = separa_palavras(texto)

    total_de_palavras = len(texto_separado)

    print(texto_separado)

    def contar_letras(texto_separado):
        total = 0
        for palavras in texto_separado:
            for letras in palavras:
                total += 1
                if letras in punctuation:
                    total -= 1
        print(total)
        return total


    tam_medio_palavra = contar_letras(texto_separado) / total_de_palavras

    relacao_type_token = n_palavras_diferentes(texto_separado) / total_de_palavras

    razao_hapax_legonama = n_palavras_unicas(texto_separado) / total_de_palavras

    tam_medio_sentença = 0

    complexidade_sentença = 0

    tam_medio_frase = 0

    print('Tamanho Médio de Palavras: ', tam_medio_palavra)

    print('Relação Type-Token: ', relacao_type_token)

    print('Razão Hapax Legonama: ', razao_hapax_legonama)

def deleta_pontos(texto):
    for caracteres in punctuation:
        texto = texto.replace(caracteres, '')
    texto = separa_palavras(texto)
    print(texto)
    return(texto)

print()
print()
print()
print()
print()
print()
calcula_assinatura('o gato caçava o rato')

print()
print()

texto_base = 'Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.'


print('texto base:')
print(texto_base)

print()
print()

print('separa sentencas: ')
print(separa_sentencas(texto_base))
a = separa_sentencas(texto_base)

new = []
for i in a:
    print()
    print('is i: ', i)
    new += separa_frases(i)
print(new)
print(len(new))
