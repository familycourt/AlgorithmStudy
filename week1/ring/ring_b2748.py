from sys import stdin
m= int(stdin.readline().strip())

list = [0,1]
for i in range(2,m+1):
    list.append(list[i-1] + list[i-2])

print(list[m])