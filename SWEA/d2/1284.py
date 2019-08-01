# 수도 요금 경쟁
t = int(input())

for tc in range(t):
    p, q, r, s, w = map(int, input().split(' '))
    charge_a = w * p
    charge_b = q if w <= r else q + (w-r) * s
    print('#{} {}'. format(tc+1, charge_b)) if charge_a > charge_b else print('#{} {}'. format(tc+1, charge_a)) 

