import cppyy

cppyy.add_include_path("../ac-library")
cppyy.cppdef("""
#include <atcoder/modint>

atcoder::modint998244353 mint(long long i){
    return atcoder::modint998244353(i);
}
""")

mi = cppyy.gbl.mint

a = mi(1)
for i in range(1, 1000001):
    a *= i
print(a.val())

# a = 1
# for i in range(1, 100000001):
#     a *= i
#     a %= 998244353
# print(a)