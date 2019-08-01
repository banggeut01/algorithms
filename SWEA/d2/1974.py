# 스도쿠 검증
# runtime error 
t = int(input())
for tc in range(1, t+1):
    # 스도쿠 한 판 저장할 1차원 리스트
    table = []
    for _ in range(10):
        table += list(map(int, input().split()))

    is_true = True
    # 가로 or 세로 or 3*3 에서 0~9 숫자 저장할 리스트
    
    # 세로 검사
    for col in range(10):
        tmp = []
        for row in range(10):
            val = table[col + row*9]
            if not val in tmp:
                tmp.append(val)
            else:
                is_true = False
                break

    if is_true:
        # 가로 검사
        for row in range(0, 81, 9):
            tmp = []
            for col in range(10):
                val = table[row+col]
                if not val in tmp:
                    tmp.append(val)
                else:
                    is_true = False
                    break
    
    if is_true:
        # 3*3 판 검사
        for start in range(0, 81, 27):
            tmp = []
            for row in range(0, 19, 9):
                for col in range(3):
                    val = table[start + row + col]
                    if not val in tmp:
                        tmp.append(val)
                    else:
                        is_true = False
                        break

    if is_true:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

