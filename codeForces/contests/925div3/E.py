import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log10, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, m = line()
    a = line()
    zeros = []
    digits = 0
    for e in a:
        z = 0
        digits += int(log10(e)) + 1
        while e%10 == 0:
            z += 1
            e //= 10
        zeros.append(z)
    zeros.sort()
    for i in range(n):
        if i%2 == 0:
            digits -= zeros[-1-i]
    if digits > m:
        print("Sasha")
    else:
        print("Anna")