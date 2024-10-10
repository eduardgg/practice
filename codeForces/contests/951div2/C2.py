
from math import lcm
for _ in range(int(input())):
    n = int(input())
    k = list(map(int, input().split()))
    harm = sum([1/e for e in k])
    if harm >= 1: print(-1)
    else:
        suma = 1
        for e in k: suma = lcm(suma, e)
        coins = [suma//e for e in k]
        if sum(coins) < suma: print(*coins)
        else: print(-1)