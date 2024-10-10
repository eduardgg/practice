import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    a.sort()
    if a[0] != a[1]:
        print("YES")
        continue
    ans = False
    for e in a:
        if e % a[0] != 0:
            ans = True
            break
    if ans:
        print("YES")
    else:
        print("NO")
