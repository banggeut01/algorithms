# 백만 장자 프로젝트
t = int(input())
for tc in range(t):
    tc_count = int(input())
    # 가격 리스트
    price_list = list(map(int, input().split()))
    # 매매차 이익
    bnf = 0
    while(len(price_list) > 1):
        idx = price_list.index(max(price_list)) + 1
        slice_list, price_list = price_list[:idx], price_list[idx:]
        for price in slice_list:
            bnf += (max(slice_list) - price)
    print('#{} {}'.format(tc+1, bnf))     
 
    