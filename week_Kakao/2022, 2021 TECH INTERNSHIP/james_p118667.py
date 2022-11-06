from collections import deque


def solution(queue1, queue2):
    s1, s2 = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    length = len(queue1 + queue2)

    if sum(queue1 + queue2) % 2 != 0:
        return -1

    result = 0

    while True:
        if not queue1 or not queue2 or result > length * 2:
            return -1
        if s1 < s2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            s2 -= tmp
            s1 += tmp
            result += 1
        elif s1 > s2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            s2 += tmp
            s1 -= tmp
            result += 1
        else:
            return result
