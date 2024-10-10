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
    s = sum(a)//n
    suma = 0
    ok = True
    for e in a:
        suma += e-s
        if suma < 0:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")