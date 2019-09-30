n = input()
def equation(n):
    o = n.count("(")
    z = n.count(")")
    if o > z:
        return ("На ", o - z, "больше '('.")
    elif z > o:
        return ("На ", z - o, "больше ')'.")
    else:
        return ("Одинаковое количество скобок.")
print(equation(n))