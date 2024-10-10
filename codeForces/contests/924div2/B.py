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
    a.sort()
    b = [a[0]]
    for e in a:
        if e != b[-1]:
            b.append(e)
    i, j = 0, 0
    millor = 0
    while j < len(b):
        if b[j]-b[i] >= n:
            i += 1
        else:
            millor = max(millor, j-i+1)
            j += 1
    print(millor)