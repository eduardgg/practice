import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
line = lambda : list(map(int,input().split()))

# Aquest codi triga més, però és més senzill
# Només cal importar una funció per trobar tots els divisors de x.
# A partir d'aquí, de gran a petit, trobem el primer vàlid.

def erathostenes(n):
    v = [0, 0] + [1]*(n-1)
    for i in range(2, n+1):
        if v[i] == 0:
            continue
        if v[i] == 1:
            j = 2*i
            while j <= n:
                v[j] = 0
                j += i
    return [p for p in range(n+1) if v[p] == 1] 

def factorize(n):
    F = {}
    primers = erathostenes(int(sqrt(n)))
    for p in primers:
        if n in primers:
            F[n] = F.get(n, 0) + 1
            break
        if p*p > n:
            break
        while n % p == 0:
            F[p] = F.get(p, 0) + 1
            n //= p
    if n != 1:
        F[n] = 1
    return F

def divisors(n):

    def f(i, d):
        if i == len(v):
            divisors.append(d)
            return
        for j in range(F[v[i]]+1):
            f(i+1, d*(v[i]**j))

    F = factorize(n)
    divisors = []
    v = []
    for k in F.keys():
        v.append(k)
    f(0, 1)
    divisors.sort()
    return divisors


for _ in range(int(input())):
    x, n = line()
    d = divisors(x)
    for i in range(len(d)):
        if n <= x//d[-1-i]:
            print(d[-1-i])
            break