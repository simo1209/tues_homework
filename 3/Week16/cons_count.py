def all_caps(s):
    count = 0
    volwels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for letter in s:
        if letter not in volwels:
            count += 1
    print count
pass
all_caps('RANdOmSTUFF')
    
