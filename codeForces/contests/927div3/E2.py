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
    ans = 0
    par = 0
    for i in range(n):
        ans *= 10
        par += int(s[i])
        ans += par
    print(ans)