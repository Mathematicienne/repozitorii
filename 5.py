''' Пользователь вводит строку вида “AxB”, где A и B какие-то числа, 
а x - арифметический знак. Нужно посчитать значение выражения. 
Допустимые арифметические знаки: +, -, /, *, //, %, **. '''

stroka = input()
arithmetic_signs = ["+", "-", "//", "**", "/", "%", "*"]

#Разделяем строку на два числа и операции
for i in arithmetic_signs:
    ii = stroka.rfind(i)
    if ii != -1:
        x = i
        A = float(stroka[: ii])
        if i == ('//' or '**'):
            B = float(stroka[ii + 2:])
        else:
            B = float(stroka[ii + 1:])
        break

#Недокалькулятор
if x == "+":
    print(A + B)
elif x == "-":
    print(A - B)
elif x == "*":
    print(A * B)
elif x == "**":
    print(A ** B)
elif x == "/":
    print(A / B)
elif x == "//":
    print(A // B)
else:
    print(A % B)