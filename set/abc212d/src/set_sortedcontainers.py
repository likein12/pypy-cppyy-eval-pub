# https://atcoder.jp/contests/abc212/tasks/abc212_d

from sortedcontainers import SortedList
import sys

def input():
    return sys.stdin.readline()[:-1]

s = SortedList()

Q = int(input())
base = 0
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0]==1:
        s.add(q[1]-base)
    elif q[0]==2:
        base += q[1]
    else:
        m = s[0]+base
        print(m)
        s.remove(m-base)
