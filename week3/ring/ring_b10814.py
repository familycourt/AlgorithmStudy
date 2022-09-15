import sys
input = sys.stdin.readline

ages = [[] for _ in range(201)]

N = int(input().strip())
for _ in range(N) :
    person = input().strip().split()
    ages[int(person[0])].append(person[1])

for i in range(201) :
    for x in ages[i] :
        print(i, x)