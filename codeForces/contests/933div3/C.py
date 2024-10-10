import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    s = input()
    mapp, pie, mapie = 0, 0, 0
    
    i = 2
    while i < n:
        if s[i-2:i+1] == 'map':
            mapp += 1
        i += 1
    
    i = 0
    while i < n-2:
        if s[i:i+3] == 'pie':
            pie += 1
        i += 1
    
    i = 0
    while i < n-4:
        if s[i:i+5] == "mapie":
            mapie += 1
        i += 1

    ans = mapp + pie - mapie
    print(ans)