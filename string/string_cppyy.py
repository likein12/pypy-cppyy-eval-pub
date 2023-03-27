import cppyy
cppyy.add_include_path("../ac-library")
cppyy.cppdef("""
#include <atcoder/string>
#include <string>
#include <iostream>
std::string inputS(){
    std::string s;
    std::cin >> s;
    return s;
}
""")

S = cppyy.gbl.inputS().decode()
SA = cppyy.gbl.atcoder.suffix_array(S)
ans =len(S) * (len(S) + 1) / 2
LCP = cppyy.gbl.atcoder.lcp_array(S, SA)
print(*LCP)