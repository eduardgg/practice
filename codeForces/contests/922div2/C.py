import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    a, b, r = line()
    if a == b:
        print(0)
        continue
    leng = max(a.bit_length() - 1, b.bit_length() - 1, 0)
    while (a & (1 << leng) == b & (1 << leng)):
        leng -= 1
    dif = (a & (1 << leng)) - (b & (1 << leng))
    leng -= 1
    while leng >= 0:
        new = (a & (1 << leng)) - (b & (1 << leng))
        if dif*new > 0 and r >= (1 << leng):
            r -= 1 << leng
            dif -= new
        else:
            dif += new
        leng -= 1
    print(abs(dif))