# 홀수만 더하기
T = int(input())

sum_num = 0
for test_case in range(T):
    num_list = list(map(int, input().split(' ')))
    for num in num_list:
        if num % 2:
            sum_num += num
    print('#{} {}'.format(test_case+1, sum_num))
    sum_num = 0
