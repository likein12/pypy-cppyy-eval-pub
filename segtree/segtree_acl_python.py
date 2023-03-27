from atcoder.segtree import SegTree
import sys
def input():
    return sys.stdin.readline()[:-1]

def op(a, b):
    return max(a,b)
e = -1

N,Q = list(map(int,input().split()))
A = list(map(int,input().split()))
seg = SegTree(op, e, A)

target = 0
def f(v):
    return v < target

for i in range(Q):
    T,A,B = list(map(int,input().split()))
    if T==1:
        seg.set(A,B)
    elif T==2:
        print(seg.prod(A,B))
    else:
        target = B
        print(seg.max_right(A,f) + 1)