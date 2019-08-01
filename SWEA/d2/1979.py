# 어디에 단어가 들어갈 수 있을까

t = int(input())

for tc in range(1, t+1):
    # n: 퍼즐의 가로 세로 길이, s: 단어의 길이
    n, s = map(int, input().split())
    puzzle = []
    # 2차원 리스트
    for _ in range(n):
        puzzle.append(list(map(int, input().split())))

    count = 0
    # 가로 검사
    for row in range(n):
        width = 0
        for col in range(n):
            # 1이면 width ++, 0이면 width = 0 하고 다음으로 넘어가기
            if puzzle[row][col]:
                width += 1
            else:
                if width == s:
                    count += 1
                width = 0
            # print(f'{row} {col}/{width}, {count}')
        if width == s:
            count += 1
        
            
    
    # 세로 검사
    for col in range(n):
        height = 0
        for row in range(n):
            # 1이면 height ++, 0이면 height = 0 하고 다음으로 넘어가기
            if puzzle[row][col]:
                height += 1
            else:
                if height == s:
                    count += 1
                height = 0
            # print(f'{row} {col}/{height}, {count}')
        if height == s:
            count += 1
            
           
    print('#{} {}'.format(tc, count))