import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, q = line()
    for i in range(n-1):
        print(i+1, i+2)
    prev = 1
    for _ in range(q):
        d = int(input())
        if d == n-1 and prev == 1:
            print("-1 -1 -1")
            continue
        if d == n-2 and prev not in {1, n-1}:
            print("-1 -1 -1")
            continue
        if d == prev:
            print("-1 -1 -1")
            continue
        else:
            print(1, prev+1, d+1)
            prev = d
