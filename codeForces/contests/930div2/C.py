import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    m = 0
    for e in range(1, n):
        print("?", m, m, e, e)
        s = input()
        if s == "<":
            m = e
    
    mm = m
    v = []
    for e in range(n):
        print("?", m, e, m, mm)
        s = input()
        if s == ">":
            v = [e]
            mm = e
        elif s == "=":
            v.append(e)
    
    # Ja tenim els elements que màximitzen el XOR
    # Anem a buscar el mínim de tots ells
    minim = v[0]
    for e in v:
        print("?", e, e, minim, minim)
        s = input()
        if s == "<":
            minim = e

    print("!", m, minim)        

