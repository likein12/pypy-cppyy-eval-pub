import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from glob import glob
import subprocess
from time import time


def match(L1, L2):
    if len(L1) != len(L2):
        return False
    else:
        f = True
        for a, b in zip(L1, L2):
            if a != b:
                f = False
                break
        return f


def test(file, txt, match=match):
    T = []
    for p in txt:
        start = time()
        cp = subprocess.run(["pypy3", file], stdin=open(
            p, "r"), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        t = time()-start
        T.append(t)
        L1 = [line for line in cp.stdout.decode().split("\n") if line != ""]
        L2 = [line.rstrip() for line in open(
            p.replace("/in/", "/out/").replace(".in", ".out"), "r") if line.rstrip() != ""]
        print(p, t, match(L1, L2))
    return T


plist = [("dsu_acl_python", "dsu_cppyy", "dsu/dsu"),
        ("fib", "fib_cppyy", "recursion/fib"),
        ("treediameter", "treediameter_cppyy", "recursion/tree_diameter"),
        ("conv_acl_python", "conv_cppyy", "convolution/convolution_mod"),
        ("set_sortedcontainers", "set_cppyy", "set/abc212d"),
        ("set_sortedcontainers", "set_cppyy", "set/abc170e"),
        ("lst_acl_python", "lst_cppyy", "lazysegtree/range_affine_range_sum"),
        ("floorsum_acl_python", "floorsum_cppyy", "math/floorsum")]


def compare(n1, n2, problem, match=match):
    src = f"{problem}/src"

    txt = glob(f"{problem}/in/*")
    txt.sort()

    T1 = test(f"{src}/{n1}.py", txt, match)
    T2 = test(f"{src}/{n2}.py", txt, match)
    lr = LinearRegression()
    lr.fit(np.array(T1).reshape(-1, 1), T2)
    a, b = lr.coef_[0], lr.intercept_
    plt.figure(figsize=(5, 5))
    plt.scatter(T1, T2)
    mx = max(max(T1), max(T2))*1.2
    plt.xlim(0, mx)
    plt.ylim(0, mx)
    plt.xlabel(n1)
    plt.ylabel(n2)
    plt.title(problem + f" y = {a:.3f}x + {b:.3f}")
    plt.plot([0, mx], [b, a*mx+b], color="orange")
    plt.savefig(f"{problem}/{n1}_vs_{n2}_1.png")
    plt.close()
    plt.scatter(T1, T2)
    plt.xlabel(n1)
    plt.ylabel(n2)
    plt.title(problem + f" y = {a:.3f}x + {b:.3f}")
    plt.plot([0, mx], [b, a*mx+b], color="orange")
    plt.savefig(f"{problem}/{n1}_vs_{n2}_2.png")
    plt.close()


for p in plist:
    compare(*p)
