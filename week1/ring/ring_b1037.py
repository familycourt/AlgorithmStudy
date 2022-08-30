#11:57 ~ 12:12

import sys

N = int(sys.stdin.readline().strip())
numbers = [int(x) for x in sys.stdin.readline().strip().split()]

# N이 1이던 홀수던 짝수던 그냥 가장 큰수 * 작은수 하면 되는건데 ..ㅎ 헷갈렷네
print(min(numbers)*max(numbers))

