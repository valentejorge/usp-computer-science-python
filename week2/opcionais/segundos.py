input_segundos = int(
    input('Por favor, entre com o número que deseja converter: '))
dia = input_segundos // 86400
hora = (input_segundos % 86400) // 3600
minuto = (input_segundos % 3600) // 60
segundo = input_segundos % 60
print(f'{dia} dias, {hora} horas, {minuto} minutos e {segundo} segundos.')
