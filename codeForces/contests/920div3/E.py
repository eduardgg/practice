import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    h, w, xa, ya, xb, yb = li()
    if xa >= xb:
        print("DRAW")
        continue
    mig = (xa+xb+1) // 2
    if (xa-xb) % 2 == 0:
        # Bob intenta guanyar. Alice intenta escapar
        if ya == yb:
            print("BOB")
        elif ya < yb:
            if yb-1 > xb-mig:
                print("DRAW")
            else:
                print("BOB")
        else:
            if w-yb > xb-mig:
                print("DRAW")
            else:
                print("BOB")
    else:
        # Alice intenta guanyar. Bob intenta escapar
        if abs(ya-yb) <= 1:
            print("ALICE")
        elif ya < yb:
            if w-ya > mig-xa:
                print("DRAW")
            else:
                print("ALICE")
        else:
            if ya-1 > mig-xa:
                print("DRAW")
            else:
                print("ALICE")