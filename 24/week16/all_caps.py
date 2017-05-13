def are_caps(word):
    are = True
    for c in word:
        if ord(c) not in range(65, 90):
            are = False
    return are
