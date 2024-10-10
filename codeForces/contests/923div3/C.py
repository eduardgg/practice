import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, m, k = line()
    a = line()
    b = line()
    ok = True
    finda, findb = [False]*k, [False]*k
    ra, rb = 0, 0
    for i in a:
        if i <= k and not finda[i-1]:
            finda[i-1] = True
            ra += 1
    for i in b:
        if i <= k and not findb[i-1]:
            findb[i-1] = True
            rb += 1
    if ra < k//2 or rb < k//2:
        print("NO")
        continue
    for i in range(k):
        if not finda[i] and not findb[i]:
            ok = False
            break
    if not ok:
        print("NO")
        continue
    print("YES")