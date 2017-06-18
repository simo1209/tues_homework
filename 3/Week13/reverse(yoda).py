def yoda(xs):
    value1=len(xs)-1
    new_xs=[]
    while 0 <= value1:
        new_xs.append(xs[value1])
        value1 -= 1
    print(new_xs)
pass
yoda(['Back', 'Harambe', 'Want', 'We'])
