'''Пользователь вводит список из целых положительных чисел. Нужно составить 
из них максимально возможное число. 
Пример: 
Ввод: 
[314, 7, 42] 
Вывод: 
742314 
Подсказка: воспользуйтесь функцией sorted(). '''

st = input()
n = ''
lst = []
for i in st:
    if (i != '[') and (i != ']'):
        if i != ',':
            n += i
        else:
            lst.append(int(n))
            n = ''
lst.append(int(n))
n = ''
lst.sort()
print(lst)
for i in range(len(lst)):
    n += str(lst[i])
print(n)

