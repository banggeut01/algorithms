# 최빈수 구하기

# f = open('./1204input.txt', 'r')
# T = int(f.readline())
T = int(input())
for _ in range(T):
    # 테스트 케이스 넘버
    test_num = int(input())
    # test_num = int(f.readline())
    # print(test_num)
    # 1000개 숫자 
    numbers = list(map(int, input().strip().split(' ')))
    '''
    strip() 안쓰면 error => 나중에 마크다운으로 정리하기
    input 파일 보면 10' '20' '30' ' 이런식으로 끝에 공백이 들어가 있음
    공백기준으로 나누기를 해서 list(map(int, f.readline().split(' ')))
    \n 엔터가 들어가버림
    해결 위해 .strip() 추가하였음
    '''
    # numbers = list(map(int, f.readline().strip().split(' ')))
    # print(numbers)
    max_num = -1
    count = -1
    # 숫자 리스트를 반복하면서
    for number in numbers:
        # 숫자의 개수를 카운팅하고 비교
        if count < numbers.count(number):
            count = numbers.count(number)
            max_num = number
        elif count == numbers.count(number) and number > max_num:
            max_num = number
    print('#{} {}'.format(test_num, max_num))
    max_num = -1
    count = -1
# f.close()