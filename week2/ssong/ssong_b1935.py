# 후위 표기식2

import sys

N = int(sys.stdin.readline())

postfix = str(sys.stdin.readline())

operand = [int(x) for x in sys.stdin.readline().split()]
diff_tmp = ord('A')

tmp_array = [0] * 30
for i in range(len(postfix)):
    if (postfix[i] >= 'A' and postfix[i] <= 'Z'):
        tmp_array[ord('postfix[i]')]

print(ord(postfix[1]) - diff_tmp)
