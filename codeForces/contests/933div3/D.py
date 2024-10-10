import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m, x = line()
    v = []
    for _ in range(m):
        e, c = input().split()
        e = int(e)
        if c == '?':
            v.append(e)
        elif c == '0':
            x = (x+e)%n
        else:
            x = (x-e)%n
    
    s = {x}
    for e in v:
        ss = set()
        for k in s:
            ss.add((k+e)%n)
            ss.add((k-e)%n)
        s = {f for f in ss}
    
    v = [(e-1)%n+1 for e in s]
    v.sort()
    print(len(v))
    print(*v)