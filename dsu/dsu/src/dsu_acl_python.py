from atcoder.dsu import DSU

N,Q = list(map(int,input().split()))

d = DSU(N)
for i in range(Q):
    t,a,b = list(map(int,input().split()))
    if t==0:
        d.merge(a,b)
    else:
        if d.leader(a) == d.leader(b):
            print(1)
        else:
            print(0)