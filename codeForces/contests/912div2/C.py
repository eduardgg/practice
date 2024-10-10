import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    suma = 0
    for i in range(n):
        suma += (i+1)*a[i]
    f = 0
    for i in range(n):
        if f < 0:
            suma -= f
        f += a[n-1-i]
    print(suma)