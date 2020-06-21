from primo import primo

n = int(input('Digite um número inteiro: '))

while n > 0:
    if primo(n):
        print(f'{n} é primo!')
    else:
        print(f'{n} não é primo :(')
    n = int(input('Digite um número inteiro: '))
