import sys
import cppyy

cppyy.add_include_path("../ac-library")
cppyy.cppdef("""
#include <atcoder/scc>
""")

readline = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
 
N, M = map(int, readline().split())
ab = list(map(int, read().split()))
 
sg = cppyy.gbl.atcoder.scc_graph(N)
 
it = iter(ab)
for a, b in zip(it, it):
    sg.add_edge(a, b)
scc = sg.scc()
n = scc.size()
print(n)
for i in range(n):
    a = scc[i]
    print(scc[i].size(), end=" ")
    for j in range(a.size()):
        print(a[j], end=" ")
    print()
