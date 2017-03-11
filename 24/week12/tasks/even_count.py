def evens_count(numbers):
    sum=0
    for num in numbers:
        if num%2==0:
            sum+=1
    return sum

print(evens_count([4,2,10,6,8,0]))