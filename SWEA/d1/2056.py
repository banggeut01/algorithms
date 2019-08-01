# 연월일 달력
m_tzero = {4, 6, 9, 11}
def calender(date):
    # 연, 월, 일 나누어 변수에 값 할당
    year = date[:4] 
    month = date[4:6]
    day = date[6:]
    # 월 예외처리
    if int(month) < 1 or int(month) > 12:
        return -1
    # 일 예외처리, 30일인 4, 6, 8, 11월
    if int(month) in m_tzero:
        if int(day) < 1 or int(day) > 30:
            return -1
    # 2월의 예외처리
    elif int(month) == 2:
        if int(day) < 1 or int(day) > 28:
            return -1
    # 나머지 1, 3, 5, 7, 8, 10, 12월 
    else:
        if int(day) < 1 or int(day) > 31:
            return -1
    return '{}/{}/{}'.format(year, month, day)


T = int(input())
for test_case in range(T):
    date = input()
    print('#{} {}'.format(test_case+1, calender(date)))
    
