# 숫자를 정렬하자
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers = sorted(numbers)
    print('#{}'.format(tc), end=" ")
    for num in numbers:
        print('{}'.format(num), end=" ")
    print('\n', end='')
    
