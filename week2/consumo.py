watts = float(input('Quantos watts eles consomem? '))
horas = float(input('Quantas horas por dias eles ficam ligados? '))
dias = float(input('Quantos dias por mês eles ficam ligados? '))
tarifa = float(input('Qual a tarifa cobrada na sua região? '))

Econsumida = (watts / 1000) * horas * dias * tarifa

print(f'o custo é R$ {Econsumida}')
