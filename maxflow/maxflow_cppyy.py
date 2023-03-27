import cppyy

cppyy.add_include_path("../ac-library")

cppyy.cppdef("""
#include <atcoder/maxflow>
int fr(atcoder::mf_graph<int>::edge &e){
    return e.from;
}
""")

N,M = list(map(int,input().split()))
S = [list(input()) for i in range(N)]
n = N*M + 2
s = N*M
t = N*M + 1
mg = cppyy.gbl.atcoder.mf_graph[int](n)
for i in range(N):
    for j in range(M):
        if S[i][j] != "#":
            if (i+j)%2==0:
                mg.add_edge(s,i*M+j,1)
                if i>0 and S[i-1][j] != "#":
                    mg.add_edge(i*M+j,(i-1)*M+j,1)
                if i<N-1 and S[i+1][j] != "#":
                    mg.add_edge(i*M+j,(i+1)*M+j,1)
                if j>0 and S[i][j-1] != "#":
                    mg.add_edge(i*M+j,i*M+j-1,1)
                if j<M-1 and S[i][j+1] != "#":
                    mg.add_edge(i*M+j,i*M+j+1,1)
            else:
                mg.add_edge(i*M+j,t,1)

print(mg.flow(s,t))

edges = mg.edges()
fr = cppyy.gbl.fr
for i in range(edges.size()):
    j = fr(edges[i])
    to = edges[i].to
    f = edges[i].flow
    if j<n-2 and to<n-2:
        if f==1:
            x,y = divmod(j,M)
            x1,y1 = divmod(to,M)
            if x1==x:
                if y<y1:
                    S[x][y] = ">"
                    S[x1][y1] = "<"
                else:
                    S[x][y] = "<"
                    S[x1][y1] = ">"
            else:
                if x<x1:
                    S[x][y] = "v"
                    S[x1][y1] = "^"
                else:
                    S[x][y] = "^"
                    S[x1][y1] = "v"
for s in S:
    print("".join(s))
