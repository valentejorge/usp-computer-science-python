lista = [2, 4, 2, 2, 3, 3, 1]

def remove_repetidos(arr):
    arr.sort()
    side = 0
    for x in arr:
        side += 1
        if side >= len(arr):
            break
        elif x == side:
            del(arr[side])
    print(arr)

remove_repetidos(lista)
