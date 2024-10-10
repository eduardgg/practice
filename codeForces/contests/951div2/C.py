
from math import lcm

for _ in range(int(input())):
    n = int(input())
    k = list(map(int, input().split()))
    harm = 0
    for e in k:
        harm += (1/e)
    if harm >= 1:
        print(-1)
    else:
        suma = 1
        for e in k: 
            suma = lcm(suma, e)
        suma -= 1
        coins = []
        for e in k:
            coins.append(suma//e + 1)
        suma = sum(coins)
        if any([k[i]*coins[i] <= suma for i in range(n)]):
            print(-1)
        else:
            print(*coins)