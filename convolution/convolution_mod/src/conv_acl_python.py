import sys
from atcoder.convolution import convolution

MOD = 998244353
N,M = map(int, sys.stdin.buffer.readline().decode().split())
A = list(map(int, sys.stdin.buffer.readline().decode().split()))
B = list(map(int, sys.stdin.buffer.readline().decode().split()))
print(*convolution(MOD, A, B))