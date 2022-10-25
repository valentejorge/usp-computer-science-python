from similaridade import n_palavras_unicas
from similaridade import n_palavras_diferentes
from similaridade import separa_palavras
from string import ascii_letters


def calcula_assinatura(texto):
    texto_separado = separa_palavras(texto)

    total_de_palavras = len(texto_separado)

    print(texto_separado)

    def contar_letras(texto_separado):
        total = 0
        for palavras in texto_separado:
            for letras in palavras:
                print(letras)
                if letras in ascii_letters:
                    total += 1
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

print()
print()
print()
print()
print()
print()
calcula_assinatura('o gato caçava o rato')
