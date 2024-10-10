import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

# Aquest codi sembla força lògic, però falla degut als "C" (don't care)
# que tenen en contacte s nodes 'S' i p nodes 'P'. Si s < p però s'escull
# primer el node 'P', es posarà més walls dels necessaris.
# Cal posar tants walls com min(s, p), i convertir 'C' en l'element més gran:
# Si s < p, 'C' passa a ser 'P', i si s > p, 'C' serà 'S' (si són iguals, no importa).

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    s = "X" + input()
    T = [[] for _ in range(n+1)]
    d = [0]*(n+1)
    status = [c for c in s]
    walls = 0
    for i in range(n-1):
        T[a[i]].append(i+2)
        T[i+2].append(a[i])
        d[a[i]] += 1
        d[i+2] += 1
    leaves = []
    for i in range(1, n+1):
        if d[i] == 1:
            leaves.append(i)
    while leaves:
        leaf = leaves.pop()
        d[leaf] -= 1
        for w in T[leaf]:
            if d[w] == 0:
                continue
            if status[w] == 'C':
                status[w] = status[leaf]
            elif (status[leaf] == 'P' and status[w] == 'S') or (status[leaf] == 'S' and status[w] == 'P'):
                    walls += 1
            d[w] -= 1
            if d[w] == 1:
                leaves.append(w)
    print(walls)