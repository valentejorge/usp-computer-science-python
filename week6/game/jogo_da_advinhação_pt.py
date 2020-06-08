from random import randint

right_number = False
computer_number = randint(0, 10)
score = 10
print('Eu estou pensando em um número entre 0 e 10.\n\nSerá que você consegue acertar?')

while right_number == False:
    player_number = int(input('tente: '))
    if player_number == computer_number:
        right_number = True
    elif player_number > computer_number:
        print('\nMuito alto!!\n')
    elif player_number < computer_number:
        print('\nMuito baixo!!\n')
    score -= 1
print('\nVocê venceu!!!\n')
print(f'Sua pontuação foi {score}\n')
if score < 4:
    print('Acho que da pra melhorar, fé em Deus!')
elif score >= 4 and score < 7:
    print('Parabéns!!')
elif score >= 7 and score < 8:
    print('Muito bem!!')
elif score == 9 and score == 8:
    print('Excelente!!!')
elif score == 10:
    print('Perfeito!!!!')
