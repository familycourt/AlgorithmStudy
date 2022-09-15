# 시간 초과 -> 다른 사람 코드 참고 

import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().strip().split()))

sort_numbers = sorted(set(numbers))

# index는 시간복잡도가 O(N)이어서 시간초과가 발생한다. 
## for number in numbers :
##     answers.append(sort_numbers.index(number))


# 해결하기 위해 dict 사용
dict_numbers = {sort_numbers[i] : i for i in range(len(sort_numbers))}
    
for number in numbers :
    print(dict_numbers[number], end=' ')

