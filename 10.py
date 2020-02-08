lst = []
for i in input().split(' '):
    lst.append(int(i))

for i in range(1, len(lst)):
    if lst[i] < lst[i-1]:
        j = i
        while lst[i] <= lst[j]:
            j -= 1
            if j == -1:
                break
        lst.insert(j + 1, lst[i])
        lst.pop(i + 1)
print(lst)


