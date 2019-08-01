# 백만 장자 프로젝트
t = int(input())
for tc_num in range(t):
    tc_count = int(input())
    price_list = list(map(int, input().split()))
    max_price = 0
    bnf = 0
    for idx in range(tc_count-1, -1, -1):
        if max_price > price_list[idx]:
            bnf += max_price - price_list[idx]
        else:
            max_price = price_list[idx]
    print('#{} {}'.format(tc_num+1, bnf)) 