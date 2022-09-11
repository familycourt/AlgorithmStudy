# 괄호

import sys

T = int(sys.stdin.readline())

# TODO: 괄호 쌍 맞춰야 할 필요 있음

for _ in range(T):
    cnt = 0
    parenthesis_string = str(sys.stdin.readline())
    for i in range(len(parenthesis_string)):
        if(parenthesis_string[i] == '('):
            cnt += 1
        if (parenthesis_string[i] == ')'):
            cnt -= 1
        if(cnt < 0):
            break
    if(cnt == 0):
        print('YES')
    else:
        print('NO')
