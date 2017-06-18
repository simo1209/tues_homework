def all_caps(s):
    state = True
    for word in s:
        if ord(word) not in range(20, 30):
            state = False
    print(state)
pass
all_caps('RANDOmSTUFF')
    
