import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def f(e):
    # Busquem el mínim índex tal que e <= v[index]
    i = bisect.bisect_left(sizes, e)
    if b[i] == 1:
        return x[i]
    else:
        return f((e-1) % (sizes[i]//(x[i]+1)) + 1)

for _ in range(int(input())):
    n, q = li()
    b, x, sizes = [], [], []
    size = 0
    for i in range(n):
        line = li()
        if size >= 10**18:
            continue
        b.append(line[0])
        x.append(line[1])
        if b[-1] == 1:
            size += 1
        else:
            size *= (x[-1] + 1)
        sizes.append(size)

    q = li()
    for e in q:
        print(f(e), end=" ")
    print()