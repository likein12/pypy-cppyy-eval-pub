import sys

def input():
    return sys.stdin.readline()[:-1]

import cppyy
cppyy.add_include_path("../ac-library")

code = """
#include <vector>
#include <atcoder/lazysegtree>
#include <atcoder/modint>
using mint = atcoder::modint998244353;

struct S {
    mint a;
    int sz;
    S(int _a, int _sz) : a(_a), sz(_sz){}
    S(mint _a, int _sz) : a(_a), sz(_sz){}
};

struct F {
    mint a, b;
    F(mint _a, mint _b) : a(_a), b(_b){}
    F(int _a, int _b) : a(_a), b(_b){}
};

S op(S l, S r) { return S{l.a + r.a, l.sz + r.sz}; }

S e() { return S{0, 0}; }

S mapping(F l, S r) { return S{r.a * l.a + r.sz * l.b, r.sz}; }

F composition(F l, F r) { return F{r.a * l.a, r.b * l.a + l.b}; }

F id() { return F{1, 0}; }

using lst_affine = atcoder::lazy_segtree<S, op, e, F, mapping, composition, id>;

void apply(lst_affine &lst, int l, int r, int a, int b){
    lst.apply(l, r, F{a,b});
}

int prod(lst_affine &lst, int l, int r){
    return lst.prod(l, r).a.val();
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

std::vector<S> getA(int n){
    std::vector<S> v;
    for(int i=0;i<n;i++){
        int a;
        scanf("%d", &a);
        v.push_back(S{a,1});
    }
    return v;
}
"""

cppyy.cppdef(code)
S = cppyy.gbl.S
F = cppyy.gbl.F
apply = cppyy.gbl.apply
prod = cppyy.gbl.prod
I = cppyy.gbl.input
N,Q = I(2)
lst = cppyy.gbl.lst_affine(cppyy.gbl.getA(N))
for i in range(Q):
    q = I(1)[0]
    if q==0:
        q = I(4)
        apply(lst,q[0],q[1],q[2],q[3])
    else:
        q = I(2)
        print(prod(lst, q[0],q[1]))
