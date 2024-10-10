import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m = line()
    if m <= n and (n+m)%2 == 0:
        print("Yes")
    else:
        print("No")