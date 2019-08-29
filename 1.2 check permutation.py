def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        d = {}
        for ch in s1:
            d[ch] = d.get(ch, 0) + 1
        for ch in s2:
            d[ch] = d.get(ch, 0) - 1
            if d[ch] < 0:
                return False
            elif d[ch] == 0:
                del d[ch]
        return True

s1 = 'abxdc'
s2 = 'bhdca'

print(check_permutation(s1, s2))