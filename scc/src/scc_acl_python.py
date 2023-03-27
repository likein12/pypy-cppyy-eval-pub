import sys
from atcoder.scc import SCCGraph

readline = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
 
N, M = map(int, readline().split())
ab = list(map(int, read().split()))
 
sg = SCCGraph(N)
 
it = iter(ab)
for a, b in zip(it, it):
    sg.add_edge(a, b)
 
scc = sg.scc()
print(len(scc))
for group in scc:
    print(str(len(group))+' '+' '.join(map(str, group)))