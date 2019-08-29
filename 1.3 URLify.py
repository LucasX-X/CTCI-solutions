def URLify(s):
    s.strip()
    return s.replace(' ', '%20')


s = 'hello  world'
print(URLify(s))
