import cppyy

cppyy.cppdef("""
long long fib(int n){
    if (n<=2) return 1;
    return fib(n-1) + fib(n-2);
}
""")

N = int(input())

print(cppyy.gbl.fib(N))