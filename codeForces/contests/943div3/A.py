from math import gcd
for _ in range(int(input())):
    n = int(input())
    topg = 0
    for x in range(1, n):
        if gcd(x, n) + x > topg:
            top = x
            topg = gcd(x, n) + x
    print(top)