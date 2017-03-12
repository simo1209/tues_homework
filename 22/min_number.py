def min_number(numbers):
    Min_now=numbers[0]
    for number in numbers:
        if Min_now>number:
            Min_now=number
    print(Min_now)

min_number([1, 2, 4])    
