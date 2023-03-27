import sys

def input():
    return sys.stdin.readline()[:-1]

import cppyy

cppyy.add_include_path("../ac-library")

cppyy.cppdef("""
#include <atcoder/math>
""")

fs = cppyy.gbl.atcoder.floor_sum

T = int(input())
for i in range(T):
    n,m,a,b = map(int,input().split())
    print(fs(n,m,a,b))