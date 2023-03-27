D = [0]*50
D[1] = 1
D[2] = 1
def fib(n):
    if D[n]!=0:
        return D[n]
    a = fib(n-1)+fib(n-2)
    D[n] = a
    return a    

for i in range(1,46):
    open(f"in/case{i}.txt", "w").write(f"{i}\n")

for i in range(1,46):
    open(f"out/case{i}.txt", "w").write(f"{fib(i)}\n")