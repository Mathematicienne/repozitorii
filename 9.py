# Сортировка пузырьком
lst = input().split(' ')
n = 1
for i in range(len(lst) + 1):
    for j in range(len(lst) - n):
        if lst[j] > lst[j+1]:
            lst[j], lst[j + 1] = lst[j +1], lst[j]
    n += 1
print(lst)
        
