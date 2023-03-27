import sys

import cppyy

cppyy.add_include_path("../ac-library")
cppyy.cppdef("""
#include <atcoder/convolution>
#include <string>
#include <vector>

std::vector<int> getIN(std::string s){
    std::vector<int> ret;
    int x = 0;
    while(x<s.size()){
        int now = 0;
        while(x<s.size()){
            int c = s[x] - '0';
            x++;
            if (c<0 || c>9) break;
            now = now*10 + c;
        }
        ret.push_back(now);
    } 
    return ret;
}
""")
MOD = 998244353
N,M = map(int, sys.stdin.buffer.readline().decode().split())
A = cppyy.gbl.getIN(sys.stdin.buffer.readline().decode())
B = cppyy.gbl.getIN(sys.stdin.buffer.readline().decode())
print(*cppyy.gbl.atcoder.convolution[MOD](A, B))
