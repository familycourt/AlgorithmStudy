# 에디터

import sys

input_string = [x for x in sys.stdin.readline().rstrip()]

command_count = int(sys.stdin.readline())


stack = []
# TODO: 문장 맨앞 맨뒤 커서 처리 확인 필요
for i in range(command_count):
    menu = [x for x in sys.stdin.readline().rstrip().split()] # 자료형 정해주지 않으면 str??
    if menu[0] == 'L' and input_string:
        stack.append(input_string.pop())
    elif menu[0] == 'D' and stack: # 맨뒤 커서
        input_string.append(stack.pop())
    elif menu[0] == 'B'and input_string:
        input_string.pop()
    elif menu[0] == 'P':
        input_string.append(menu[1])

input_string.extend(reversed(stack)) # 참신하고 어렵다..
print(''.join(input_string))
