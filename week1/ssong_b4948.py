# 베르트랑 공준

import sys

#에라토스테네스의 체 활용 필요



def eratosthenes_sieve(N):
    #전체 체 초기화 : 모두 소수로 가정
    sieve = [True] * (N + 1)
    
    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i * 2, N + 1, i): # (시작범위, 마지막 범위, range 간격)
                sieve[j] = False
                
    true_count = sum(sieve) -1

    return [i for i in range(2, N+1) if sieve[i] == True]

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    print(len(eratosthenes_sieve(2 * N)) - len(eratosthenes_sieve(N)))
 