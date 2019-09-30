n = dict(zip('abc', input().split()))
def dict_key(n):
    k = []
    v = 0
    for key, val in n.items():
        if int(val) == v:
            k.append(key)
            v = int(val)
        elif int(val) > v:
            k.clear()
            k.append(key)
            v = int(val)
    return(k)
print(dict_key(n))


