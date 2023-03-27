import sys

def input():
    return sys.stdin.readline()[:-1]

from sortedcontainers import SortedList
from collections import defaultdict

whole = SortedList()
dcms = defaultdict(SortedList)

N, Q = list(map(int,input().split()))
A = []
B = [] 
s = set()
for i in range(N):
    a,b = list(map(int,input().split()))
    A.append(a)
    B.append(b)
    dcms[b].add(a)
    s.add(b)

for i in s:
    whole.add(dcms[i][-1])
 
for i in range(Q):
    c,d = list(map(int,input().split()))
    a = A[c-1]
    b = B[c-1]
    B[c-1] = d
    fr = dcms[b]
    to = dcms[d]
    fr_max = fr[-1]
    whole.remove(fr_max)
    fr.remove(a)
    if len(fr)!=0:
        whole.add(fr[-1])
    if len(to)!=0:
        to_max = to[-1]
        whole.remove(to_max)
    to.add(a)
    whole.add(to[-1])
    print(whole[0])