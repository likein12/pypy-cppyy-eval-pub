import sys

def input():
    return sys.stdin.readline()[:-1]

from atcoder.lazysegtree import LazySegTree

MOD = 998244353

def op(a,b):
    return ((a[0]+b[0])%MOD, a[1]+b[1])
e = (0, 0)
def mapping(f, a):
    return ((f[0]*a[0]+f[1]*a[1])%MOD, a[1])
def composition(f, g):
    return (f[0]*g[0]%MOD, (g[1]*f[0]+f[1])%MOD)

id_ = (1,0)

N,Q = list(map(int,input().split()))
A = list(map(int,input().split()))
v = [(a,1) for a in A]

lst = LazySegTree(op,e,mapping,composition,id_,v)

for i in range(Q):
    q = list(map(int,input().split()))
    if q[0]==0:
        lst.apply(q[1],q[2],(q[3],q[4]))
    else:
        print(lst.prod(q[1],q[2])[0])
