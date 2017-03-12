def max_number(numbers):
    Max_now=numbers[0]
    for number in numbers:
        if Max_now<number:
            Max_now=number
    print(Max_now)

max_number([1, 2, 4])

    
