ni = int(input('Numero: '))
na = ni % 3
nb = ni % 5
if na == 0 and nb == 0:
    print ('FizzBuzz')
else:
    print (ni)
