# 최빈수
T = int(input())
for _ in range(T):
    # 테스트 케이스 넘버
    tc = int(input())
    # split(' ')으로 지정해주지 않아도 된다.
    numbers = list(map(int, input().split()))
    # 점수는 0~100, 0부터 시작해 카운트가 더 큰 값을 mode_num으로 지정해주면 된다.
    mode_num = 0
    mode_count = numbers.count(0)
    for score in range(1, 101):
        if numbers.count(score) >= mode_count:
            mode_num = score
            mode_count = numbers.count(score)
    print('#{} {}'.format(tc, mode_num))