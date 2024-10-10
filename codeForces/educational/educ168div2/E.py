import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict, Counter
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
for _ in range(q):
    i, x = list(map(int, input().split()))
    