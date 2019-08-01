# 파리 퇴치
fly_matrix = []
t = int(input())
for tc in range(1, t+1):
    m, n = list(map(int, input().split()))
    for _ in range(m):
        fly_matrix += list(map(int, input().split())) # 2차원 리스트 아닌 1차원 리스트로
    kill = sum(fly_matrix[0:n][0:n]) # 수정하기
    for i in range(m-n+1):
        for j in range(1, m-n+1):
            print(sum(fly_matrix[i:i+n][j:j+n]))
