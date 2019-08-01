# 간단한 소인수분해
t = int(input())
primes = [2, 3, 5, 7, 11]
for tc in range(1, t+1):
    result = []
    num = int(input())
    for prime in primes:
        quot, mod = divmod(num, prime)
        count = 0 # 소인수 개수 카운트
        while not mod: # 나머지 0 일 동안
            count += 1
            num = quot
            quot, mod = divmod(num, prime)
        result.append(str(count))
    print('#{} {}'.format(tc, ' '.join(result)))
