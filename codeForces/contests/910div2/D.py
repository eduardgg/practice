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
    b = line()
    dif = 0
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
        dif += (b[i]-a[i])
    dif += 2*max(max(a)-min(b), 0)
    print(dif)