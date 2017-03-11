def tail(arr):
    new_arr = []
    i = 1
    while i < len(arr):
        new_arr.append(arr[i])
        i += 1
    return new_arr


print(tail([]))
