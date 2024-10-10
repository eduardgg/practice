import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, x, y = line()
    a = line()
    ans = 0
    d = {}
    for e in a:
        ans += d.get(((-e)%x, e%y), 0)
        d[(e%x, e%y)] = d.get((e%x, e%y), 0) + 1
    print(ans)