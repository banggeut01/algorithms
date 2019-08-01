T = int(input())
for test_case in range(T):
    a, b = map(int, input().split(' '))
    print('#{} {} {}'.format(test_case+1, int(a/b), a%b))