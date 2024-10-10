import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    m = int(input())
    a = line()
    b = line()
    c = []
    for i in range(m):
        c.append((a[i], b[i]))
    c.sort()
    for i in range(m):
        print(c[i][0], end=" ")
    print()
    for i in range(m):
        print(c[i][1], end=" ")
    print()