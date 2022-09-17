# 쇠막대기
# 모르겠다.. 수정의 수정 다시보기
import sys

stack = [x for x in sys.stdin.readline().rstrip()]

tmp_stack = []
total_count = 0
tmp_count = 1
for a in stack:
    if a == '(':
        tmp_stack.append(a)
    elif a == ')':
        if tmp == '(':
            tmp_stack.pop()
            total_count += len(tmp_stack)
        else:
            total_count += 1
            tmp_stack.pop()
    tmp = a

print(total_count)
