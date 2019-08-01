# 중간값 찾기
T = int(input())
num_list = list(map(int, input().split(' ')))
num_list = sorted(num_list)
mid_pos = int(len(num_list) / 2)
print(num_list[mid_pos])