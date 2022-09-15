import sys
input = sys.stdin.readline

sortnums = [1,2,3,4,5]

nums = list(map(int, input().strip().split()))

while nums != sortnums :
    for i in range(4) :
        if nums[i] > nums[i+1] :
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(' '.join(map(str, nums)))    

