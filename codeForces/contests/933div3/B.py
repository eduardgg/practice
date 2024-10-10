import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    ok = True
    for i in range(n-2):
        if a[i] < 0:
            ok = False
            break
        k = a[i]
        a[i] -= k
        a[i+1] -= 2*k
        a[i+2] -= k
    if not ok or a[n-2] != 0 or a[n-1] != 0:
        print("NO")
    else:
        print("YES")