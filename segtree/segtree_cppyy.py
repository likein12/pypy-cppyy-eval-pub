import cppyy
cppyy.add_include_path("../ac-library")

cppyy.cppdef("""
#include <atcoder/segtree>
#include <cstdio>
#include <vector>
int op(int a, int b) { return std::max(a, b); }
int e() { return -1; }
int target;
bool f(int v) { return v < target; }

using segtree = atcoder::segtree<int,op,e>;

std::vector<int> input(int n){
    std::vector<int> g;
    int a;
    for(int i=0;i<n;++i){
        scanf("%d", &a);
        g.push_back(a);
    }
    return g;
}

segtree getseg(int n){
    std::vector<int> a(n);
    for(int i=0;i<n;++i){
        scanf("%d", &(a[i]));
    }
    return segtree(a);
}

int max_right(segtree &seg, int p, int t){
    target = t;
    return seg.max_right<f>(p);
}
""")
inp = cppyy.gbl.input
N,Q = inp(2)
seg = cppyy.gbl.getseg(N)
max_right = cppyy.gbl.max_right

for i in range(Q):
    T, A, B = inp(3)
    if T==1:
        seg.set(A,B)
    elif T==2:
        print(seg.prod(A,B))
    else:
        print(max_right(seg, A, B) + 1)