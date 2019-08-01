# 1대1 가위바위보
a, b = map(int, input().split(' '))

if a == 3 and  b == 1:
    print('B')
elif b == 3 and a == 1:
    print('A')
elif a > b:
    print('A')
else:
    print('B')

