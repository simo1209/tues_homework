def max_number(numbers):
    currentMin=numbers[0]
    for num in numbers:
        if currentMin<num:
            currentMin=num
    return currentMin

print(max_number([5,12]))