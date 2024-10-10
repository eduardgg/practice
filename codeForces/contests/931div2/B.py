import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

v = [0,1,2,1,2,3,1,2,3,2,1,2,2,2,3,1,2,3,2,3,2,2,3,3,3,2,3,3,3,4,2]
for _ in range(int(input())):
    n = int(input())
    ans = 0
    if n > 30:
        inc = (n-15)//15
        ans += inc
        n -= 15*inc
    ans += v[n]
    print(ans)
