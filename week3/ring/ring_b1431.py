import string
import sys
input = sys.stdin.readline

N = int(input().strip())
guitars = []
for _ in range(N) :
    guitars.append([_ for _ in input().strip() ])

for i in reversed(range(1, N)) :
    for j in range(i) :
        if len(guitars[j]) > len(guitars[j+1]) :
            guitars[j], guitars[j+1] = guitars[j+1], guitars[j]
        elif len(guitars[j]) < len(guitars[j+1]) :
            continue
        else :
            cnt0, cnt1 = 0, 0
            for x in guitars[j] :
                if x in string.digits :
                    cnt0 += int(x)
            for x in guitars[j+1] :
                if x in string.digits :
                    cnt1 += int(x)
            
            if cnt0 > cnt1 :
                guitars[j], guitars[j+1] = guitars[j+1], guitars[j]
            elif cnt0 < cnt1 :
                continue
            else :
                for k in range(len(guitars[j])) :
                    if guitars[j][k] > guitars[j+1][k] :
                        guitars[j], guitars[j+1] = guitars[j+1], guitars[j]
                        break
                    elif guitars[j][k] < guitars[j+1][k] :
                        break

for guitar in guitars :
    print(''.join(map(str, guitar)))