# 큰 놈, 작은 놈, 같은 놈
T = int(input())
for test_case in range(T):
    num_list = list(map(int, input().split(' ')))
    if num_list[0] < num_list[1]:
        expression = '<'
    elif num_list[0] > num_list[1]:
        expression = '>'
    else:
        expression = '='
    print('#{} {}'.format(test_case+1, expression))
