def xor(a, b):
    if a == 'True':
        if b == 'True':
            print('False')
        if b == 'False':
            print('True')
    elif a == 'False':
        if b == 'True':
            print('False')
        if b == 'False':
            print('True')
    else:
        print('Syntax Error!')
pass

a=str(input('A State (True/False):'))
b=str(input('B State (True/False):'))
xor(a, b)
