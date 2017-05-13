def volwels_count(word):
    res=0
    volwels = ['A','E','I','O','U','a','e','i','o','u']
    for c in word:
        if c in volwels:
            res+=1
    return res

#print(volwels_count("hello"))