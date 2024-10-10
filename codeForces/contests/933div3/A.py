import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m, k = line()
    a = line()
    b = line()
    a.sort()
    b.sort()
    i, j = 0, m-1
    ans = 0
    while i < n and j >= 0:
        if a[i]+b[j] > k:
            j -= 1
        else:
            ans += (j+1)
            i += 1
    print(ans)
