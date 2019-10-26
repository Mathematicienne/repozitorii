''' Пользователь вводит текст. Вывести самое длинное слово и наиболее 
часто встречаемое слово. '''

counter = {}
text = input().split()
for word in text:
    counter[word] = counter.get(word, 0) + 1
    #counter[word] = [counter.get(word, 0) + 1, counter.get(word, len(word))]
n = max(counter.values())
lst = []
for key, val in counter.items():
    if val == n:
        lst.append(key)
print('Самое(ые) наиболее встречаемое(ые) слово(а):', ", ".join(lst))

counter1 = {}
for word in text:
    counter1[word] = counter1.get(word, len(word))
n1 = max(counter.values())
lst1 = []
for key, val in counter.items():
    if val == n1:
        lst1.append(key)
print('             Самое(ые) длинное(ые) слово(а):', ", ".join(lst1))

