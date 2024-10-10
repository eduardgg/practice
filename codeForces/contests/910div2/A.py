import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, k = line()
    s = input()
    count = 0
    for e in s:
        if e == 'B':
            count += 1
    if count == k:
        print(0)
    else:
        print(1)
        if count < k:
            c = 0
            i = 0
            while c < k-count:
                if s[i] == 'A':
                    c += 1
                i += 1
            print(i, 'B')
        else:
            c = 0
            i = 0
            while c < count-k:
                if s[i] == 'B':
                    c += 1
                i += 1
            print(i, 'A')
