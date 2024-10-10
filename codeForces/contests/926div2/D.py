
line = lambda : list(map(int,input().split()))
mod = 998244353

for _ in range(int(input())):
    n = int(input())
    g = [[] for _ in range(n+1)]
    d = [0] * (n+1)
    for _ in range(n-1):
        u, v = line()
        g[u].append(v)
        g[v].append(u)
        d[u] += 1
        d[v] += 1
    q = []
    for i in range(n+1):
        if d[i] == 1:
            q.append(i)
    dp = [1] * (n+1)
    ans = 1
    i = 0
    while i < len(q):
        v = q[i]
        d[v] -= 1
        for u in g[v]:
            if d[u] == 0:
                ans += dp[u]
                ans %= mod
                continue
            d[u] -= 1
            dp[u] *= (dp[v] + 1)
            dp[u] %= mod
            if d[u] == 1:
                q.append(u)
        i += 1
    ans += dp[q[-1]]
    ans %= mod
    print(ans)