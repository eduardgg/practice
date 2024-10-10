import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    n, f, a, b = li()
    m = li()
    i = 0
    now = 0
    while f > 0 and i < n:
        f -= min((m[i]-now)*a, b)
        now = m[i]
        i += 1
    if f <= 0:
        print("NO")
    else:
        print("YES")
