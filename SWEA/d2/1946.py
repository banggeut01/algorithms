# 간단한 압축 풀기
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    result = ''
    print('#{}'.format(tc))
    for _ in range(n):
        char, num = input().split()
        num = int(num)
        result += char*num
    while result:
        if len(result) >= 10:
            print(result[:10])
            result = result[10:]
        else:
            print(result)
            result = None

    