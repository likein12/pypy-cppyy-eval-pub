# https://atcoder.jp/contests/abc212/tasks/abc212_d

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
    T get_min(std::multiset<T> &s){ return *s.begin(); }
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

ms = cppyy.gbl.mset["long long"]()
Q = int(input())
base = 0
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0]==1:
        ms.insert(q[1]-base)
    elif q[0]==2:
        base += q[1]
    else:
        m = ms.pop_min()+base
        print(m)
