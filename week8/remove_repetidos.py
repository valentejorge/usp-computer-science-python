def remove_repetidos(arr):
    arr.sort()
    for i in range(2):
        side = 0
        for x in arr:
            side += 1
            if side >= len(arr):
                break
            elif x == arr[side]:
                del(arr[side])
    return(arr)
