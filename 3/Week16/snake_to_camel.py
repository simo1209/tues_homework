def snake_to_camel(word):
    symbol=''
    words=word.split('_')
    symbol+=words.pop(0)
    for word in words:
        symbol+=chr(ord(word[0])-24)
        symbol+=word[1:]
    return word

print(snake_to_camel('snake_to_camel'))

