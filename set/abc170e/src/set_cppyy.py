import cppyy
import sys

def input():
    return sys.stdin.readline()[:-1]

cppyy.cppdef("""
#include <set>
template<class T>
struct mset {
    std::multiset<T> s;
    mset(){
        s = std::multiset<T>();
    }
    void insert(T n){ s.insert(n); }
    void erase(T n){ s.erase(s.find(n)); }
    bool contain(T n){ return s.find(n) != s.end(); }
    T get_max(){ return *s.rbegin(); }
    T get_min(){ return *s.begin(); }
    T pop_max(){
        auto it = s.rbegin();
        T m = *it;
        s.erase(--(it.base()));
        return m;
    }
    T pop_min(){
        auto it = s.begin();
        T m = *it;
        s.erase(it);
        return m;
    }
    T lower_bound(T n){ return *s.lower_bound(n); }
    T upper_bound(T n){ return *s.upper_bound(n); }
    int size(){ return s.size(); }
};
""")

from collections import defaultdict

whole = cppyy.gbl.mset["int"]()
dcms = defaultdict(cppyy.gbl.mset["int"])

N, Q = list(map(int,input().split()))
A = []
B = [] 
s = set()
for i in range(N):
    a,b = list(map(int,input().split()))
    A.append(a)
    B.append(b)
    dcms[b].insert(a)
    s.add(b)

for i in s:
    whole.insert(dcms[i].get_max())
 
for i in range(Q):
    c,d = list(map(int,input().split()))
    a = A[c-1]
    b = B[c-1]
    B[c-1] = d
    fr = dcms[b]
    to = dcms[d]
    fr_max = fr.get_max()
    whole.erase(fr_max)
    fr.erase(a)
    if fr.size()!=0:
        whole.insert(fr.get_max())
    if to.size()!=0:
        to_max = to.get_max()
        whole.erase(to_max)
    to.insert(a)
    whole.insert(to.get_max())
    print(whole.get_min())