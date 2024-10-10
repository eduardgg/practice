import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

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

# Implementació meva, retorna la factorització d'un
# nombre n en forma de diccionari (nombre de factors)
def factorize(n):
    F = {}
    for p in primes:
        if n in primes:
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


line = lambda : list(map(int,input().split()))
primes = erathostenes(32000)
for _ in range(int(input())):
    n, x = line()
    f1 = divisors(n-x)
    f2 = divisors(n+x-2)
    ks = set()
    for f in f1+f2:
        if f%2 != 0:
            continue
        e = f//2 + 1
        if e >= x:
            ks.add(e)
    print(len(ks))