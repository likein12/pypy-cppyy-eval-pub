import sys

def input():
    return sys.stdin.readline()[:-1]

from atcoder.math import floor_sum

T = int(input())
for i in range(T):
    n,m,a,b = map(int,input().split())
    print(floor_sum(n,m,a,b))