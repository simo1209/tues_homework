def reverse(arr):
    i = len(arr) - 1
    new_arr = []
    while 0 <= i:
        new_arr.append(arr[i])
        i -= 1
    return new_arr


print(reverse([1, 2, 3]))
