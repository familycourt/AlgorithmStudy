import sys
input = sys.stdin.readline

T = int(input().strip())
for i in range(T) : 
    str = input().strip()

    # 닫는 것 + , 여는 것 -
    cnt = 0
    for j in reversed(range(len(str))) :
        tmp = str[j]
        if cnt == 0:
            if tmp == '(' :
                cnt = -1
                break

        if tmp == ')' :
            cnt += 1
        else :
            cnt -= 1

    if cnt == 0 :
        print('YES')
    else :
        print('NO')