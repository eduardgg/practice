import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

lletres = "abcdefghijklmnopqrstuvwxyz"
g = {lletres[i]:i for i in range(26)}

for _ in range(int(input())):
    n, m = line()
    s = input()
    t = input()

    ok = True
    pos = [deque() for _ in range(26)]
    for i in range(n):
        pos[g[s[i]]].append(i)
    for ll in t:
        if len(pos[g[ll]]) == 0:
            ok = False
            break
        p = pos[g[ll]].popleft()
        for e in range(g[ll]):
            while len(pos[e]) > 0 and pos[e][0] < p:
                pos[e].popleft()
    
    if ok:
        print("YES")
    else:
        print("NO")