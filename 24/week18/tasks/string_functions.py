def avoids(word, forbidden_letters):
    """
    Напишете функция, която приема като аргумент дума `word` и списък от
    забранени символи.
    Функцията трябва да връща като резултат `True`, ако думата не съдържа нито един
    от забранените символи.
    """

    for c in forbidden_letters:
        if c in word:
            return False
    return True
    pass


assert avoids('program', 'xyz')
assert not avoids('program', 'pqr')


def uses_only(word, letters):
    """
    Напишете функция, която приема като аргумент дума `word` и списък от символи.
    Функцията трябва да връща като резултат `True`, ако думата съдържа само символи
    от списъка.
    """
    for letter in letters:
        if letter not in word:
            return False
    return True
    pass


assert uses_only('program', 'progam')
assert not uses_only('program', 'mxyz')


def uses_all(word, letters):
    """
    Напишете функция, която приема като аргумент дума `word` и списък от символи.
    Функцията трябва да връща като резултат `True`, ако думата съдържа всеки от
    символите от списъка поне веднъж.
    """
    for letter in letters:
        if letter not in word:
            return False
    return True
    pass


assert uses_all('program', 'progam')
assert not uses_all('program', 'progamxyz')
