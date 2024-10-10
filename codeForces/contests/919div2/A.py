import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    prohibits = set()
    minim = 1
    maxim = 10**9
    for _ in range(int(input())):
        a, x = li()
        if a == 1:
            minim = max(minim, x)
        elif a == 2:
            maxim = min(maxim, x)
        else:
            prohibits.add(x)
    dolents = 0
    for e in prohibits:
        if e <= maxim and e >= minim:
            dolents += 1
    if minim > maxim:
        print(0)
    else:
        print(maxim - minim + 1 - dolents)