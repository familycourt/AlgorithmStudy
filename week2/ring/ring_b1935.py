import sys
import string
input = sys.stdin.readline

N = int(input().strip())
str = input().strip()

nums=[]
for i in range(N) :
    nums.append(int(input().strip()))

numbers = []
operators = []
for i in range(len(str)) :
    tmp = str[i]
    if tmp in string.ascii_uppercase :
        numbers.append(nums[ord(tmp) - ord('A')])
    else :
        n = numbers.pop()
        m = numbers.pop()
        if tmp == '*' :
            numbers.append(n*m)
        elif tmp == '/':
            numbers.append(m/n)
        elif tmp == '+' :
            numbers.append(n+m)
        elif tmp == '-' :
            numbers.append(m-n)

print(f'{numbers[0]:.2f}')