# 지그재그 숫자

t = int(input())

for tc in range(1, t+1):
    result = 0
    flag = -1
    num = int(input())
    for i in range(1, num+1):
        flag *= -1
        result += i * flag
    print('#{} {}'.format(tc, result))

# 실행시간 더 느림
# for tc in range(1, t+1):
#     result = 0
#     num = int(input())
#     if num % 2:
#         result = (num-1)/2 * (-1) + num
#     else:
#         result = num/2*(-1)
#     print('#{} {}'.format(tc, int(result)))