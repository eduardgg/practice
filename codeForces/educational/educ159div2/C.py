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
    g = 0
    for i in a[1:]:
        g = gcd(g, i-a[0])
    if g == 0: print(1); continue

    ops = 0
    s = set()
    for i in a:
        o = (a[-1]-i)//g
        ops += o
        s.add(o)
    i = 0
    while True:
        if i not in s:
            ops += i
            break
        i += 1

    print(ops)