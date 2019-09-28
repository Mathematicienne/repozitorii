n = int(input())
if n % 3 == 0:
    if n % 5 ==0:
        print('Fizz Buzz')
    else:
        print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(str(n))
