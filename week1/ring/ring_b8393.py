# 입출력을 빠르게 하는 .. 어쩌구 저쩌구..
from sys import stdin

# strip() : 양쪽 공백 날려줌
n = int(stdin.readline().strip())

m = (1+n)*n/2

print(int(m))

