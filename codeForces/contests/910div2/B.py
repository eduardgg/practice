import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    ops = 0
    maxim = a[-1]
    for i in range(n):
        if a[n-1-i] <= maxim:
            maxim = a[n-1-i]
            continue
        sep = a[n-1-i] // maxim
        if a[n-1-i] % maxim == 0:
            sep -= 1
        ops += sep
        maxim = a[n-1-i] // (sep + 1)
    print(ops)