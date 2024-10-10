import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    s = input()
    suma, sumb = 0, 0
    for e in s:
        if e == 'A':
            suma += 1
        else:
            sumb += 1
    if suma > sumb:
        print('A')
    else:
        print('B')