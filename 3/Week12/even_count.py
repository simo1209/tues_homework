def evens_count(nums):
    count=0
    for num in nums:
        if num%2==0:
            count+=1
    return count

pass

print(evens_count([1,2,3,4,5,69,420]))
