def encryption(text, keys):
    # Получение координат букв в изначальном тексте
    x = ""
    y = ""
    for i in text:
        if i in keys:
            x += str(keys[i] // 10)
            y += str(keys[i] % 10)
    sum_num = x + y
 
    # Получение координат в зашифрованном тексте
    x = ""
    y = ""
    for i in range(len(sum_num)):
        if not (i % 2):
            x += sum_num[i]
        else:
            y += sum_num[i]
 
    # Шифрование и вывод текста
    text = ""
    for i in range(len(x)):
        sum_num = int(x[i] + y[i])
        for key, val in keys.items():
            if val == sum_num:
                text += key
    return(text)
 
 
def decryption(code_text, keys):
    # Получение координат для дешифрования
    sum_num = ""
    for i in code_text:
        sum_num += str(keys[i])
    len_num = int(len(sum_num) / 2)
    x = ""
    y = ""
    for i in range(len_num):
        x += sum_num[i]
        y += sum_num[i + len_num]
 
    # Дешифрование
    text = ""
    for i in range(len(x)):
        sum_num = int(x[i] + y[i])
        for key, val in keys.items():
            if val == sum_num:
                text += key
    return(text)
 
 
with open("./text.txt", 'r') as f:
    text = f.read()
print("Объем текста: ", len(text))
print("    Пробелов: ", text.count(" "))

# Преобразование текста
text = text.lower()
text = text.replace("j", "i")
 
# Сам ключ
keys = dict(zip(["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                [11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55]))
 
code_text = encryption(text, keys)
text = decryption(code_text, keys)
print(" Объем зашифрованного текста: ", len(code_text))
print("Объем расшифрованного текста: ", len(text))

with open("./encryption.txt", 'w') as f:
    f.write(code_text)
with open("./decryption.txt", "w") as f:
    f.write(text)

