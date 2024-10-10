import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    trobat, trobat2 = False, False
    num = 0
    for _ in range(n):
        s = input()
        if not trobat:
            for e in s:
                if e == '1':
                    trobat = True
                    num += 1
        elif not trobat2:
            trobat2 = True
            num2 = 0
            for e in s:
                if e == '1':
                    num2 += 1
            if num == num2:
                ans = "SQUARE"
            else:
                ans = "TRIANGLE"
    print(ans)