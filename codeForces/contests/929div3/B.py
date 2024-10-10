import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    uns = False
    suma = 0
    for e in a:
        if e%3 == 1:
            uns = True
        suma += e

    if suma%3 == 0:
        print(0)
    elif suma%3 == 2:
        print(1)
    else:
        if uns:
            print(1)
        else:
            print(2)