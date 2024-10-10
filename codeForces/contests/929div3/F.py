import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m = line()
    a = []
    for _ in range(n):
        a.append(line())

    i, j = 0, 0
    t = 0
    seg = 0
    ok = True
    while j < m-1:
        if not a[(i+t+1)%n][j+1]:
            j += 1
            seg = 0
        elif a[(i+t+1)%n][j] or a[(i+t+2)%n][j]:
            ok = False
            break
        else:
            i += 1
            seg += 1
            if seg > n//2:
                ok = False
                break
        t += 1
    if not ok:
        print(-1)
        continue
    i %= (n-1)
    t += min(n-1-i, i+1)
    print(t)