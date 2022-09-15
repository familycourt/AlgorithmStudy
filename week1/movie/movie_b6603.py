import sys
from itertools import combinations


while(True):
    testCase = list(map(int, sys.stdin.readline().split()))

    k = testCase.pop(0)

    if k == 0:
        break

    for cases in combinations(testCase, 6):
        print(' '.join(map(str, cases)))

    print()
