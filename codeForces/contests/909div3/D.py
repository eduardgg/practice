import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    g = {}
    for e in a:
        g[e] = g.get(e, 0) + 1
    suma = g.get(1, 0) * g.get(2, 0)
    for i in g.keys():
        suma += g[i]*(g[i]-1)//2
    print(suma)