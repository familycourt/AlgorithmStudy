# reverse 사용하여 queue 뒤집으면 시간초과 -> 코드 참고
## 해결법 안 뒤집고 cnt 이용하여 pop()과 popleft() 사용하면 댐 ㄷㄷ 

# 그리고 숫자를 int로 재정의 할 필요가 있는지 없는지 생각해보자. 여기서는 필요 없다는거 ~
#아스키 코드 사용 : string -> 숫자를 그대로 써서 쓸모 없어짐.. (미안)
import sys
input = sys.stdin.readline
from collections import deque

T = int(input().strip())
for _ in range(T) :
    commands = [str(x) for x in input().strip()]
    n = int(input().strip())
    arr = input().strip()[1:-1].split(',')
    if n>0 : queue = deque(arr)
    else : queue = deque([])

    cnt = 0 
    flag =0
    for command in commands :
        if command == 'R' :
            cnt+=1
        elif command == 'D' :
            if not queue :
                print('error')
                flag = 1
                break
            else :
                if cnt%2 == 0 : queue.popleft()
                else : queue.pop()

    if cnt%2 == 1 :
        queue.reverse()
    if flag == 0:
        print('[' + ','.join(queue) + ']')

    