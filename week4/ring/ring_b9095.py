import sys
input = sys.stdin.readline

nlist = []

T = int(input().strip())
for _ in range(T) :
    n = int(input().strip())
    nlist.append(n)

# 앞의 1,2,3은 본인 스스로도 정답이므로 포함시켜줘야한다.
nums = [0,1,2,4] + [0 for _ in range(4, max(nlist)+1)]
for i in range(4, max(nlist)+1) :
    nums[i] = nums[i-3] + nums[i-2] + nums[i-1]

for n in nlist :
    print(nums[n])