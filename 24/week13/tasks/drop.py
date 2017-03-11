def drop(n, arr):
    new_arr = arr
    for i in range(n):
        new_arr.pop(0)
    return new_arr


print(drop(2, [5, 8, 1, 2]))
