
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    t = [[] for _ in range(n)]
    for _ in range(n-1):
        x, y = list(map(int, input().split()))
        t[x-1].append(y-1)
        t[y-1].append(x-1)
    dfs = [0]
    stack = [0]
    parent = [-1]*n
    dp = [-1]*n
    dpn = [-1]*n
    while stack:
        u = stack.pop()
        if len(t[u]) == 1:
            dp[u] = a[u]
        for v in t[u]:
            if v != parent[u]:
                parent[v] = u
                dfs.append(v)
                stack.append(v)
    
    dp1, dp2, dp3 = [-1]*n, [-1]*n, [-1]*n
    for u in dfs[::-1]:
        dp1[u] = 1*a[u] + sum([min(dp2[v], dp3[v]) for v in t[u] if v != parent[u]])
        dp2[u] = 2*a[u] + sum([min(dp3[v], dp1[v]) for v in t[u] if v != parent[u]])
        dp3[u] = 3*a[u] + sum([min(dp1[v], dp2[v]) for v in t[u] if v != parent[u]])
    
    ans = min(dp1[0], dp2[0], dp3[0])
    print(ans)