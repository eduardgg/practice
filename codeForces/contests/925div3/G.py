import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

def mod_inverse(x, m):
    _, result, _ = extended_gcd(x, m)
    return result % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def bin(n, k, m):
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(1, min(k, n - k) + 1):
        result = (result * (n - i + 1) % m) * mod_inverse(i, m) % m
    return result



MOD = 998244353
line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    c1, c2, c3, c4 = line()
    c = max(c1, c2)
    
    if c == 0:
        if c3 * c4 > 0:
            print(0)
        else:
            print(1)
        continue

    if abs(c1-c2) > 1:
        ans = 0
    
    elif c1 == c2:
        ans = bin(c3+c, c, MOD) * bin(c4+c-1, c-1, MOD)
        ans += bin(c3+c-1, c-1, MOD) * bin(c4+c, c, MOD)

    else:
        ans = bin(c3+c-1, c-1, MOD) * bin(c4+c-1, c-1, MOD)
    
    ans %= MOD
    print(ans)