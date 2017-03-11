def take(num,arr):
    new_arr = []
    for i in range(num):
        new_arr.append(arr[i])
    return new_arr

print(take(3,[3,4,0,0,0,0]))