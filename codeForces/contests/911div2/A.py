import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    s = input()
    seguits = 0
    punts = 0
    magia = False
    for i in range(n):
        if s[i] == '.':
            punts += 1
            seguits += 1
        else:
            seguits = 0
        
        if seguits == 3:
            magia = True
            break
    
    if magia:
        print(2)
    else:
        print(punts)