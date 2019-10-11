# Ввод текста
text = input()

# Преобразование текста к нижнему регистру
text = text.lower()
#text = text.replace("j", "i")

# Сам ключ
a = dict(zip(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
             [11, 12, 13, 14, 15, 21, 22, 23, 24, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55]))

# Получение координат букв в изначальном тексте
x = ""
y = ""
for i in text:
    if i in a:
        x = x[::] + str(a[i] // 10)
        y = y[::] + str(a[i] % 10)
c = x + y

# Получение координат в зашифрованном тексте
x = ""
y = ""
for i in range(len(c)):
    if i % 2 == 0:
        x = x[::] + c[i]
    elif i % 2 == 1:
        y = y[::] + c[i]

# Шифрование и вывод текста
text = ""
for i in range(len(x)):
    c = int(x[i]) * 10 + int(y[i])
    for key, val in a.items():
        if val == c:
            text = text[::] + key
print(text)

# Получение координат для дешифрования
x = ""
y = ""
for i in text:
    if i in a:
        x = x[::] + str(a[i] // 10)
        y = y[::] + str(a[i] % 10)
c = x + y

k = len(c) / 2
k = int(k)
x1 = c[:k]
y1 = c[k:]
x = ""
y = ""
n = 0
m = 0
for i in range(k):
    if i % 2 == 0:
        x = x[::] + x1[n]
        n += 1
    else:
        x = x[::] + y1[m]
        m += 1
for i in range(1, k + 1):
    if i % 2 == 0:
        y = y[::] + x1[n]
        n += 1
    else:
        y = y[::] + y1[m]
        m += 1

# Дешифровка и вывод текста
text = ""
for i in range(len(x)):
    c = int(x[i]) * 10 + int(y[i])
    for key, val in a.items():
        if val == c:
            text = text[::] + key
print(text)
