# 중간 평균값 구하기
t = int(input())

for tc in range(1, t+1):
    numbers = list(map(int, input().split()))
    numbers.remove(min(numbers))
    numbers.remove(max(numbers))
    print('#{} {}'.format(tc, round(sum(numbers)/len(numbers))))