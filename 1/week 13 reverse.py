Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def reverse(xs):
    i = len(xs) - 1
    new_xs = []
    while 0<=i:
        new_xs.append(xs[i])
        i -= 1
    return new_xs

>>> print(reverse([1, 2, 3]))
[3, 2, 1]
>>> 
