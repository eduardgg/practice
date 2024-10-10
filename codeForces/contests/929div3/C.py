import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    a, b, l = line()
    s = set()
    i = 0
    while (l % (a**i) == 0):
        j = 0
        nl = l//(a**i)
        while (nl % (b**j) == 0):
            s.add(nl//(b**j))
            j += 1
        i += 1
    print(len(s))