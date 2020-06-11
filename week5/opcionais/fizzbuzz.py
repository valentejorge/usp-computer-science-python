def fizzbuzz(ni):
    na = ni % 3
    nb = ni % 5

    if na == 0 and nb == 0:
        return ('FizzBuzz')
    elif na == 0:
        return ('Fizz')
    elif nb == 0:
        return ('Buzz')
    else:
        return (ni)
