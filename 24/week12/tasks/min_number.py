def min_numbers(numbers):
    currentMin=numbers[0]
    for num in numbers:
        if currentMin>num:
            currentMin=num
    return currentMin

print(min_numbers([5,12]))