import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, k = line()
    a = line()
    if k >= 2:
        print("YES")
        continue
    ok = True
    for i in range(n-1):
        if a[i+1] < a[i]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
