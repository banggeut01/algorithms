# 앞선 방법보다 실행시간 더 길다.
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    count = 0
    print('#{}'.format(tc))
    for _ in range(n):
        char, num = input().split()
        num = int(num)
        for i in range(num):
            print(char, end="")
            count += 1
            if count == 10:
                print('\n', end="")
                count = 0
    print('\n', end="")