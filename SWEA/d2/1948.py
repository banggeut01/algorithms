# 날짜 계산기
t = int(input())
calen = {}

input_value = '1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31'
values = list(input_value.split(', '))
for value in values:
    mon, day = map(int, value.split('/'))
    calen[mon] = day


for tc in range(1, t+1):
    mon1, day1, mon2, day2 = map(int, input().split())
    if mon1 == mon2: # 같은달이면
        result = day2 - day1 + 1
    else:
        result = day2 + calen[mon1] - day1 + 1
        for i in range(mon2-1, mon1, -1): # 8월 5월이면, 7 ~ 6월까지.
            result += calen[i]
    print('#{} {}'.format(tc, result))
