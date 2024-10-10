import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    a.sort()
    suma = 0
    reps = 1
    count1 = 0
    count2 = 0
    if a[0] == 1:
        count1 += 1
    elif a[0] == 2:
        count2 += 1
    for i in range(1, len(a)):
        if a[i] == 1:
            count1 += 1
        elif a[i] == 2:
            count2 += 1
        if a[i] == a[i-1]:
            reps += 1
        else:
            suma += reps*(reps-1)//2
            reps = 1
    suma += count1 * count2
    suma += reps*(reps-1)//2
    print(suma)