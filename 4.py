x,y=float(input()),float(input())
if x>0 and y>0:
    print('I')
elif x>0 and y<0:
    print('IV')
elif x<0 and y<0:
    print('III')
elif x<0 and y>0:
    print('II')
else:
    print('x=0 or y=0')