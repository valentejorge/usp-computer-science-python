def maximo(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    elif c > a and c > b:
        return c
    elif a == b == c:
        return a
