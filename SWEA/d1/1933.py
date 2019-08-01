# 아주 간단한 약수
T = int(input())
for i in range(1, T+1):
    if not T % i:
        print(i, end=' ')