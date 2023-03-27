import sys

sys.setrecursionlimit(500000)

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
Graph = [[] for i in range(N)]
for i in range(N-1):
    a,b,c = list(map(int,input().split()))
    Graph[a].append((b,c))
    Graph[b].append((a,c))
DP = [-1]*N
par = [-1]*N
DP[0] = 0

def dfs(v):
    d = DP[v]
    for v1,d1 in Graph[v]:
        if DP[v1]<0:
            DP[v1] = d+d1
            par[v1] = v
            dfs(v1)
dfs(0)

mx = 0
mxi = 0
for i in range(N):
    if DP[i] > mx:
        mxi = i
        mx = DP[i]
for i in range(N):
    DP[i] = -1
DP[mxi] = 0
dfs(mxi)
mx = 0
mxi1 = 0
for i in range(N):
    if DP[i] > mx:
        mx = DP[i]
        mxi1 = i
ans = [mxi1]

while mxi1!=mxi:
    mxi1 = par[mxi1]
    ans.append(mxi1)
print(mx, len(ans))
print(*ans)