import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    n = int(input())
    s = input()
    f = input()
    x, y = 0, 0
    for i in range(len(s)):
        if s[i] == f[i]:
            continue
        if s[i] == '1':
            x += 1
        if s[i] == '0':
            y += 1
    print(max(x, y))