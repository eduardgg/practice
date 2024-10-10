
for _ in range(int(input())):
    n = int(input())
    g = [[0 for _ in range(n)] for _ in range(n)]
    a = []
    for _ in range(n):
        a.append(input().split())
    for i in range(n):
        for j in range(i):
            if a[i][0] == a[j][0] or a[i][1] == a[j][1]:
                g[i][j] = g[j][i] = 1
    
    dp = [[False for _ in range(n)] for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = True
    
    top = 0
    for i in range(1 << n):
        for j in range(n):
            if dp[i][j]:
                top = max(top, bin(i).count('1'))
                for k in range(n):
                    if not i & (1 << k) and g[j][k]:
                        dp[i | (1 << k)][k] = True

    ans = n - top
    print(ans)