# 조교의 성적 매기기
t = int(input())

levels = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, t+1):
    n, s = map(int, input().split()) # n: 학생수, s: 알고 싶은 학생
    scores = [] # 평점 저장할 리스트
    for i in range(1, n+1):
        sco1, sco2, sco3 = map(int, input().split())
        result = sco1*35 + sco2*45 + sco3*20
        scores.append(result)
        if i == s: # 알고 싶은 학생 점수 기억하기
            stu = result

    scores = sorted(scores)[::-1] # 점수순으로 정렬
    idx = scores.index(stu) + 1
    idx = idx / int((n/10))

    # 정수이면
    if int(idx)==idx:
        print('#{} {}'.format(tc, levels[int(idx)-1]))
    else:
        print('#{} {}'.format(tc, levels[int(idx)]))
        
    # runtime error
    # print('#{} {}'.format(tc, levels[scores.index(stu)]))
    
    # n이 10일때만
    # for sco, lev in zip(scores, levels):
    #     if sco == stu:
    #         print('#{} {}'.format(tc, lev))

    # runtime error
    # idx = math.ceil((scores.index(stu)+1) / (n/10))
    # print('#{} {}'.format(tc, levels[idx-1]))

