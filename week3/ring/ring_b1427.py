import sys
input = sys.stdin.readline

N = [int(x) for x in input().strip()]
N.sort(reverse=1)

print(''.join(map(str, N)))