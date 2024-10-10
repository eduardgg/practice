import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

def query(i, j):
    i += le - 1
    j += le - 1
    mini = minind[i]
    maxi = maxind[i]
    while i <= j:
        if i%2 == 1:
            if a[minind[i]] < a[mini]:
                mini = minind[i]
            if a[maxind[i]] > a[maxi]:
                maxi = maxind[i]
            i += 1
        if j%2 == 0:
            if a[minind[j]] < a[mini]:
                mini = minind[j]
            if a[maxind[j]] > a[maxi]:
                maxi = maxind[j]
            j -= 1
        i //= 2
        j //= 2
    return mini + 1, maxi + 1

for _ in range(int(input())):
    n = int(input())
    a = line()
    q = int(input())

    le = 2**(n-1).bit_length()
    minind = [-1]*le + [i for i in range(n)] + [-1]*(le-n)
    maxind = [-1]*le + [i for i in range(n)] + [-1]*(le-n)
    k = le
    while k >= 1:
        for i in range(k, 2*k):
            if minind[i//2] == -1 or a[minind[i//2]] > a[minind[i]]:
                minind[i//2] = minind[i]
            if maxind[i//2] == -1 or a[maxind[i//2]] < a[maxind[i]]:
                maxind[i//2] = maxind[i]
        k //= 2
    for _ in range(q):
        l, r = line()
        minim, maxim = query(l, r)
        if a[minim-1] == a[maxim-1]:
            print(-1, -1)
        else:
            print(minim, maxim)