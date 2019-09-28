n = int(input())
a = n*2-1
lst=[]
for i in range(1,a+1,2):
    lst.append(' ' * int((a - i)/2) + '*' * i + ' ' * int((a - i)/2))
print("\n".join(lst))