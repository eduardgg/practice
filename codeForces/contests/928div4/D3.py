import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))
num = (1<<31) - 1
for _ in range(int(input())):
    n = int(input())
    a = line()
    a.sort()
    grups = 0
    i, j = 0, n-1
    while i < j:
        grups += 1
        if a[i] == num - a[j]:
            i += 1
            j -= 1
        elif a[i] < num - a[j]:
            i += 1
        else:
            j -= 1
    if i == j:
        grups += 1
    print(grups)