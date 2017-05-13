def caps_count(word):
    res = 0
    for c in word:
        if ord(c) in range(65, 90):
            res += 1
    return res
