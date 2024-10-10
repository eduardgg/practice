import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
line = lambda : list(map(int,input().split()))

# Òbviament falla per time limit:
# x pot arribar a ser molt gran (10**8), i no és eficient
# restar 1 a cada iteració, ja que pot arribar a 1 si és primer.

for _ in range(int(input())):
    x, n = line()
    k = x // n
    while x % k != 0:
        k -= 1
    print(k)