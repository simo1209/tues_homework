def max_number(numbers):
    minNum=numbers[0]
    for num in numbers:
        if minNum<num:
            minNum=num
        else:
            pass
    return minNum

pass

print(max_number([144, 60, 1337, 8]))
