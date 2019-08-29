def is_unique(s) -> bool:
    check = 0

    for ch in s:
        if check & 1 << ord(ch) > 0:
            return False
        check = check | 1 << ord(ch)
    return True

s = 'qweqrty'

print(is_unique(s))