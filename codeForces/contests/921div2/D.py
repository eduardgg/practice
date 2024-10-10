import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt


def mod_inv(x, m):
    _, result, _ = extended_gcd(x, m)
    return result % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x
    
line = lambda : list(map(int,input().split()))
mod = 10**9 + 7

for _ in range(int(input())):
    n, m, k = line()
    s = 0
    for _ in range(m):
        a, b, f = line()
        s += f

    # Càlcul de la fórmula usant esperances condicionades
    p = 2*s*k*n*(n-1) + 2*m*k*(k-1)
    q = n*n*(n-1)*(n-1)
    g = gcd(p, q)
    p, q = p//g, q//g
    print(p*mod_inv(q, mod) % mod)
