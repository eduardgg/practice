import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(str, input().split()))

for _ in range(int(input())):
    n = int(input())
    trump = input()[0]
    cards = line()

    v = {}
    for c in cards:
        v[c[1]] = v.get(c[1], []) + [c]

    tipus = 0
    for k in v.keys():
        v[k].sort()
        if k != trump:
            tipus += (len(v[k]) % 2)
    
    if tipus > len(v.get(trump, [])):
        print("IMPOSSIBLE")
        continue

    left = []
    for k in v.keys():
        if k == trump:
            continue
        for i in range(len(v[k])//2):
            print(v[k][2*i], v[k][2*i+1])
        if len(v[k]) % 2 == 1:
            left.append(v[k][-1])
    
    i = 0
    for e in left:
        print(e, v[trump][i])
        i += 1

    while i < len(v.get(trump, [])):
        print(v[trump][i], v[trump][i+1])
        i += 2