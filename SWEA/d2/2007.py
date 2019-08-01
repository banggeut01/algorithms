# 패턴 마디의 길이
t = int(input())
for tc in range(1, t+1):
    string = input()
    for i in range(1, 11):
        if string.count(string[:i]) == int(30/i) and if string[:i*int(30/i)] == string[:i]*string.count(string[:i]):
            print('#{} {}'.format(tc, i))
            break

