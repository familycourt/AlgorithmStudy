# 로또

import sys
import itertools

while True:
    a = [int(x) for x in sys.stdin.readline().split()]

    k = a[0]
    if k == 0:
        break

    input_arr = [int(a) for index, a in enumerate(a) if index != 0]
    result_arr = list(itertools.combinations(input_arr, 6))
    for i in result_arr:
        print(*i)
    print()
