import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    x0, y0 = li()
    for _ in range(3):
        x, y = li()
        if x > x0:
            x1 = x
        elif x < x0:
            x1 = x0
            x0 = x
        if y > y0:
            y1 = y
        elif y < y0:
            y1 = y0
            y0 = y  
    print((x1-x0)*(y1-y0))