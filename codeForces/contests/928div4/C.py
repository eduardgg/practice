import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

v = [0]
for i in range(1, 200001):
    suma = 0
    while i > 0:
        suma += (i%10)
        i //= 10
    v.append(v[-1] + suma)

for _ in range(int(input())):
    n = int(input())
    print(v[n])