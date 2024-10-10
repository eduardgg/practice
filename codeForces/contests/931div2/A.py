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
    ans = 2*(a[-1]+a[-2]-a[0]-a[1])
    print(ans)