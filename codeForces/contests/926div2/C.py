import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    k, x, a = line()
    if a <= x:
        print("NO")
        continue
    ok = True
    s = 0
    for i in range(x):
        A = s//(k-1) + 1
        s += A
        if s >= a:
            ok = False
            break
    if not ok:
        print("NO")
        continue
    if (a-s)*(k-1) - s > 0:
        print("YES")
    else:
        print("NO")