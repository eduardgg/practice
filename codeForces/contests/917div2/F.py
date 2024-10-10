import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

def knapsack(m, pes):
    if pes == 0:
        return True
    if pes < 0 or m < 0:
        return False
    if dp[m][pes] != -1:
        return dp[m][pes]
    dp[m][pes] = knapsack(m-1, pes-l[m-1]) or knapsack(m-1, pes)


for _ in range(int(input())):
    n, d = line()
    l = line()
    dp = [[-1 for _ in range(d+1)] for _ in range(n+1)]
    k = knapsack(n, d)
