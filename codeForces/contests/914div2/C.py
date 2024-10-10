import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    a = line()
    if k >= 3:
        print(0)
        continue
    a.sort()
    if k == 1:
        minim = a[0]
        for i in range(n-1):
            minim = min(minim, a[i+1]-a[i])
        print(minim)
        continue
    # k = 2
    difs = set()
    for i in range(n):
        for j in range(i+1, n):
            difs.add(a[j]-a[i])
    minim = min(a[0], min(difs))
    for d in difs:
        i = bisect.bisect_left(a, d)
        if i > n:
            minim = min(minim, d-a[-1])
        elif i == 0:
            minim = min(minim, a[0]-d)
        else:
            minim = min(minim, a[i]-d, d-a[i-1])
    print(minim)