import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    n, m = li()
    a = li()
    b = li()
    a.sort()
    b.sort()
    la = 0
    ra = n-1
    lb = 0
    rb = m-1
    dif = 0
    for _ in range(n):
        if b[rb]-a[la] > a[ra]-b[lb]:
            dif += (b[rb]-a[la])
            rb -= 1
            la += 1
        else:
            dif += (a[ra]-b[lb])
            ra -= 1
            lb += 1
    print(dif)