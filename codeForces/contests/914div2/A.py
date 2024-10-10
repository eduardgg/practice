import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt


line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    a, b = line()
    xk, yk = line()
    xq, yq = line()
    suma = 0
    if a == b:
        dirs = [(a,a),(a,-a),(-a,a),(-a,-a)]
    else:
        dirs = [(a,b),(a,-b),(-a,b),(-a,-b),(b,a),(b,-a),(-b,a),(-b,-a)]
    for (x1, y1) in dirs:
        for (x2, y2) in dirs:
            if xk+x1==xq+x2 and yk+y1==yq+y2:
                suma += 1
    print(suma)