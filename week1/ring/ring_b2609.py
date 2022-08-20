from sys import stdin

# 유클리드 호제법을 사용했다 ~

# 최대공약수
def gcd(n, m):
    if n%m == 0 : return m
    else : return gcd(m, n%m)

# 최대 공배수
def lcm(n, m):
    return n*m/gcd(n, m)

x = stdin.readline().split()
N, M = int(x[0]), int(x[1])


print(gcd(N, M))
print(int(lcm(N, M)))