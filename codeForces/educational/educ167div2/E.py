import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))