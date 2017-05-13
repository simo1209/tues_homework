def snake_to_pascal(word):
    words=word.split('_')
    res = ''
    for word in words:
        res+=chr(ord(word[0])-32)
        res+=word[1:]
    return res

print(snake_to_pascal('hello_world'))
