def all_caps(s):
    count = 0
    for letter in s:
        if ord(letter) not in range(20, 30):
            count += 1
    print(count)
pass
all_caps('RANdOmSTUFF')
    
