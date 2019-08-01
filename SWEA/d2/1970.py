# 쉬운 거스름돈
t = int(input())
units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, t+1):
    result = []
    won = int(input())
    for unit in units:
        quot, won = divmod(won, unit)
        result.append(quot)
    print('#{}'.format(tc))
    print(' '.join(list(map(str, result))))
    