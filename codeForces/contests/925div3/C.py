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
    esq = 0
    dre = 0
    for e in a:
        if e == a[0]:
            esq += 1
            continue
        break
    for e in a[::-1]:
        if e == a[-1]:
            dre += 1
            continue
        break
    if a[0] == a[-1]:
        print(max(n-esq-dre, 0))
    else:
        print(n-max(esq, dre))