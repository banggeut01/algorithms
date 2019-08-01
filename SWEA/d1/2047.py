# 신문 헤드라인 .upper()
string = input()
headline = ''

for i in range(len(string)):
    if ord(string[i:i+1]) >= 97 and ord(string[i:i+1]) <= 122:
        headline += chr(ord(string[i:i+1]) - 32)
    else:
        headline+= string[i:i+1]
print(headline)