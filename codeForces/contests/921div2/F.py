import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
line = lambda : list(map(int,input().split()))
mod = 999999893

def mod_exp(b, e, m):
    result = 1
    bin_exp = bin(e)[2:]
    for bit in bin_exp[::-1]:
        if bit == '1':
            result = (result * b) % m
        b = (b * b) % m
    return result

def mod_inv(x, m):
    _, result, _ = extended_gcd(x, m)
    return result % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x
    
for _ in range(int(input())):
    x = int(input())
    if x % 2 == 1:
        k = (x-1) // 2
        p = (mod_exp(2, k, mod) - 1) % mod
        q = ((mod_exp(2, k, mod) + 1)**2 - 2) % mod
    else:
        k = x // 2
        p = (2 * (1 - mod_exp(2, k, mod))) % mod
        q = ((mod_exp(2, k, mod) - 2)**2 - 2) % mod
    print((p * mod_inv(q, mod)) % mod)
