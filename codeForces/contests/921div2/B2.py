import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
line = lambda : list(map(int,input().split()))

# Aquest codi és més eficient, busca els divisors de x: O(sqrt(x))
# De totes maneres només passa a CodeForces amb PyPy, i no Python.

for _ in range(int(input())):
    x, n = line()
    i = 1
    ans = 1
    while i*i <= x:
        if x%i == 0:
            if n <= x//i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x//i)
        i += 1
    print(ans)