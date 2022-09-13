import sys
input = sys.stdin.readline


N = int(input().strip())
nums = [0,0,1,1,2,3] + [0 for _ in range(6, N+1)]

for i in range(6, N+1) :
    tmp =[]
    if i%3==0 :
        tmp.append(nums[i//3]+1)
    if i%2==0 :
        tmp.append(nums[i//2]+1)
    tmp.append(nums[i-1]+1)
    nums[i] = min(tmp)

print(nums[N])