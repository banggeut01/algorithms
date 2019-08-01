# 평균값 구하기
T = int(input())
sum_num = 0

for test_case in range(T):
     num_list = list(map(int, input().split(' ')))
     for num in num_list:
          sum_num += num
          avg = round(sum_num / len(num_list))
     print('#{} {}'.format(test_case+1, avg))
     sum_num = 0
