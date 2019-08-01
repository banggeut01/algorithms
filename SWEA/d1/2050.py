# 알파벳을 숫자로 변환

string = input()
for i in range(len(string)):
    num = ord(string[i:i+1]) - 64
    print('{} '.format(num), end='')