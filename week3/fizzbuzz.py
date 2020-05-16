ni = int(input('Número: '))
na = ni % 3
nb = ni % 5

if na == 0 and nb == 0:
    print('FizzBuzz')
elif na == 0:
    print('Fizz')
elif nb == 0:
    print('Buzz')
else:
    print(ni)
