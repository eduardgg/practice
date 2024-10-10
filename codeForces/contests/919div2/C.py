import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())


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
        # L'últim factor (fora del vector "primers", l'assumim primer)
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


primers = erathostenes(500)
for _ in range(int(input())):
    n = int(input())
    d = divisors(n)
    print(d)
    a = li()
    result = 0
    for i in d:
        m = 0
        for j in range(n-i):
            m = gcd(m, abs(a[j]-a[j+i]))
            if m == 1:
                break
        if m != 1:
            result += 1
    print(result)