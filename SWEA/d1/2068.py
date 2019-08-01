# 최대수 구하기
T = int(input())

for test_case in range(T):
    num_list = list(map(int, input().split(' ')))
    max_num = num_list[0]
    for num in num_list[1:]:
        if num > max_num:
            max_num = num
    print('#{} {}'.format(test_case+1, max_num))