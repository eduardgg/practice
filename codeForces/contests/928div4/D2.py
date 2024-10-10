import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))
num = (1<<31) - 1
for _ in range(int(input())):
    n = int(input())
    a = line()
    a.sort()
    d = {}
    grups = 0
    for e in a:
        if d.get(num-e, 0) > 0:
            d[num-e] -= 1
        else:
            grups += 1
            d[e] = d.get(e, 0) + 1
    print(grups)