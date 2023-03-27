import sys

def input():
    return sys.stdin.readline()[:-1]

import cppyy

cppyy.cppdef("""
#include <vector>
#include <utility>

using Graph = std::vector<std::vector<std::pair<int, long long>>>;
Graph g(500000);
long long DP[500000];
int par[500000];

void dfs(int v){
    long long d = DP[v];
    for(auto [v1,d1]: g[v]){
        if (DP[v1]<0){
            DP[v1] = d+d1;
            par[v1] = v;
            dfs(v1);
        }
    }
}
std::vector<int> input(int n){
    std::vector<int> g;
    int a;
    for(int i=0;i<n;++i){
        scanf("%d", &a);
        g.push_back(a);
    }
    return g;
}

void inputG(int n){
    for(int i=0;i<n;++i){
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);    
        g[a].push_back({b,c});
        g[b].push_back({a,c});
    }
}
""")

N = cppyy.gbl.input(1)[0]
cppyy.gbl.inputG(N-1)
DP = cppyy.gbl.DP

for i in range(N):
    DP[i] = -1
DP[0] = 0
cppyy.gbl.dfs(0)
mx = 0
mxi = 0
for i in range(N):
    if DP[i] > mx:
        mxi = i
        mx = DP[i]
for i in range(N):
    DP[i] = -1
DP[mxi] = 0
cppyy.gbl.dfs(mxi)
mx = 0
mxi1 = 0
for i in range(N):
    if DP[i] > mx:
        mx = DP[i]
        mxi1 = i
par = cppyy.gbl.par
ans = [mxi1]

while mxi1!=mxi:
    mxi1 = par[mxi1]
    ans.append(mxi1)
print(mx, len(ans))
print(*ans)

