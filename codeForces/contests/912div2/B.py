import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    M = [[] for _ in range(n)]
    a = []
    for i in range(n):
        M[i] = line()
        a.append(M[i][(i+1)%n])
        for j in range(n):
            if j != i:
                a[-1] &= M[i][j]
    ok = True
    for i in range(n):
        for j in range(n):
            if i != j and M[i][j] != a[i]|a[j]:
                ok = False
                break
        if not ok:
            break
    if not ok:
        print("NO")
    else:
        print("YES")
        print(*a)
        