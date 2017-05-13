def snake_to_camel(word):
    res=''
    words=word.split('_')
    res+=words.pop(0)
    for word in words:
        res+=chr(ord(word[0])-32)
        res+=word[1:]
    return res

print(snake_to_camel('snake_to_camel'))