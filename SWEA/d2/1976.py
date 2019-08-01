# 시각 덧셈
t = int(input())
for tc in range(1, t+1):
    h1, m1, h2, m2 = map(int, input().split())
    quota = (m1+m2) // 60 
    mode = (m1+m2) % 60
    hour = (h1+h2+quota) % 12
    if hour == 0:
        hour = 12
    minu = mode
    print('#{} {} {}'.format(tc, hour, minu))