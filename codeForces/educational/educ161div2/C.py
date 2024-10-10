import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    n = int(input())
    a = li()
    m = int(input())

    dreta = [-1]*n
    suma = 0
    for i in range(n-2, 0, -1):
        if a[i+1] - a[i] > a[i] - a[i-1]:
            suma += a[i+1] - a[i]
        else:
            suma += 1
        dreta[i] = suma
    dreta[0] = suma + 1
    dreta[-1] = 0

    esq = [-1]*n
    suma = 0
    for i in range(1, n-1):
        if a[i+1] - a[i] < a[i] - a[i-1]:
            suma += a[i] - a[i-1]
        else:
            suma += 1
        esq[i] = suma
    esq[-1] = suma + 1
    esq[0] = 0

    for _ in range(m):
        xi, yi = li()
        if xi < yi:
            print(dreta[xi-1] - dreta[yi-1])
        else:
            print(esq[xi-1] - esq[yi-1])
        