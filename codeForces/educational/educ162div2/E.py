import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict, Counter
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    c = [0] + line()
    T = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = line()
        T[u].append(v)
        T[v].append(u)

    parent = [0]*(n+1)
    order = [1]
    for e in order:
        for v in T[e]:
            if v != parent[e]:
                order.append(v)
                parent[v] = e
    order = order[::-1]
    order.pop()

    ans = 0
    dp = [Counter() for _ in range(n+1)]
    for e in range(n+1):
        dp[e][c[e]] = 1
    for u in order:
        dp[u][c[u]] = 1
        p = parent[u]

        # Aquest fragment és per eficiència:
        if len(dp[p]) < len(dp[u]):
            dp[p], dp[u] = dp[u], dp[p]
        
        for k in dp[u]:
            ans += dp[p][k] * dp[u][k]
            dp[p][k] += dp[u][k]
        dp[p][c[p]] = 1
    
    print(ans)