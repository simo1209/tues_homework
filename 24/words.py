from random import randint


# Добавете думи тук
words = [
    'apple',
    'banana'
]


def get_random_word():
    """
    Дефинирайте функция, която връща произволна дума от списъка
    """
    return words[randint(0,len(words)-1)]
    pass


def fill_char(char, word, original_word):
    res=""
    """
    Дефинирайте функция, която добавя познатата буква към думата `word`.
    Напр.:
        >>> original_word = 'apple'
        >>> word = '_____'
        >>> word = fill_char('p', word, original_word)
        >>> word
        _pp__
    """
    c=0
    while c < len(original_word):
        if original_word[c] is char:
            res+=char
        else:
            res+=word[c]
        c+=1
    return res
    print(res)
    pass


if __name__ == '__main__':
    original_word = get_random_word()
    word = '_' * len(original_word)
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in original_word:
            word = fill_char(char, word, original_word)
            print(word)
