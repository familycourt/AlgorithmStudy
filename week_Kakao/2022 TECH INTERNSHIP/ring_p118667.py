# 진짜.. 댕빡세다.. 후... 
import sys
from collections import deque
input = sys.stdin.readline

def solution(q1, q2):
    cnt=0
    sum1 = sum(q1)
    sum2 = sum(q2)
    queue1 = deque(q1)
    queue2 = deque(q2)
    
    if (sum1+sum2)%2 != 0 : return -1
    
    while True :
        if not queue1 or not queue2 or cnt > (len(q1)+len(q2))*2:
            return -1
        
        if sum1 == sum2 :
            return cnt
        elif sum1 < sum2 :
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            cnt += 1
        else :
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum2 += tmp
            sum1 -= tmp
            cnt += 1
            
queue1 = list(map(int, input().strip().split()))
queue2 = list(map(int, input().strip().split()))

print(solution(queue1, queue2))