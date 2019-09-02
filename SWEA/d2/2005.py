# 2005.py 파스칼의 삼각형

t = int(input())
for tc in range(1, t + 1):
    print('#{}'.format(tc))
    n = int(input())

    tmp1 = [] # 이전 행 저장 리스트
    tmp2 = [] # 임시 저장 리스트
    for i in range(1, n + 1): # 행
        for j in range(1, i + 1):
            if j == 1 or j == i: # 처음, 끝
                tmp2.append(1)
                print(1, end=' ')
            else:
                num = tmp1[j - 2] + tmp1[j - 1]
                tmp2.append(num)
                print(num, end=' ')
        print()
        tmp1, tmp2 = tmp2, []