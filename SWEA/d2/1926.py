# 간단한 369게임
number = int(input())
result = ''
for num in range(1, number+1):
    num = str(num)
    if '3' in num or '6' in num or '9' in num:
        result += '-' * (num.count('3') + num.count('6') + num.count('9')) + ' '
    else:
        result += num + ' '
print(result)