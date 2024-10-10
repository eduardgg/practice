
from math import gcd

for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    h = []
    for _ in range(n):
        h.append(list(map(int, input().split())))
    snow = []
    for _ in range(n):
        snow.append(input())

    curDif = 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        sumr = 0
        for j in range(m):
            sumr += 2*int(snow[i][j]) - 1
            dp[i+1][j+1] = dp[i][j+1] + sumr
            curDif += h[i][j] * (1 if snow[i][j]=='1' else -1)
    curDif = abs(curDif)
    
    g = 0
    for i in range(n-k+1):
        for j in range(m-k+1):
            opt = dp[i+k][j+k] - dp[i][j+k] - dp[i+k][j] + dp[i][j]
            g = gcd(g, opt)
    
    if not curDif or (g and not curDif%g):
        print("YES")
    else:
        print("NO")