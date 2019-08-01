# 자릿수 더하기
result = 0

number = input()
for i in range(len(number)):
    result += int(number[i:i+1])

print(result)
