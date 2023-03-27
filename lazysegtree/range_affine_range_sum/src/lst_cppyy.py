import cppyy
import sys

def input():
    return sys.stdin.readline()[:-1]


cppyy.add_include_path("../ac-library")

code = """
#include <vector>
#include <atcoder/lazysegtree>
#include <atcoder/modint>
using mint = atcoder::modint998244353;

struct S {
    mint a;
    int sz;
};

struct F {
    mint a, b;
};

S op(S l, S r) { return S{l.a + r.a, l.sz + r.sz}; }

S e() { return S{0, 0}; }

S mapping(F l, S r) { return S{r.a * l.a + r.sz * l.b, r.sz}; }

F composition(F l, F r) { return F{r.a * l.a, r.b * l.a + l.b}; }

F id() { return F{1, 0}; }

using lst_affine = atcoder::lazy_segtree<S, op, e, F, mapping, composition, id>;

std::vector<S> getA(std::vector<int> &orig){
    std::vector<S> v;
    for(int i=0;i<orig.size();i++){
        v.push_back(S{orig[i],1});
    }
    return v;
}

void apply(lst_affine &lst, int l, int r, int a, int b){
    lst.apply(l, r, F{a,b});
}

int prod(lst_affine &lst, int l, int r){
    return lst.prod(l, r).a.val();
}
"""

cppyy.cppdef(code)
S = cppyy.gbl.S
F = cppyy.gbl.F
apply = cppyy.gbl.apply
prod = cppyy.gbl.prod

N, Q = list(map(int, input().split()))
v = cppyy.gbl.getA(cppyy.gbl.std.vector[int](list(map(int, input().split()))))
lst = cppyy.gbl.lst_affine(v)
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        apply(lst, q[1], q[2], q[3], q[4])
    else:
        print(prod(lst, q[1], q[2]))
