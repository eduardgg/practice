
for _ in range(int(input())):
    n, c = list(map(int, input().split()))
    a = [-1] + list(map(int, input().split()))
    g = [[] for _ in range(n+1)]
    parent = [-1]*(n+1)
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        g[u].append(v)
        g[v].append(u)
    stack = [1]
    dfs = [1]
    while stack:
        u = stack.pop()
        for v in g[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)
                dfs.append(v)
    dp1, dp2 = [-1]*(n+1), [-1]*(n+1)
    while dfs:
        u = dfs.pop()
        dp1[u] = sum([max(dp1[v], dp2[v]) for v in g[u] if v != parent[u]])
        dp2[u] = a[u] + sum([max(dp1[v], dp2[v] - 2*c) for v in g[u] if v != parent[u]])
    ans = max(dp1[1], dp2[1])
    print(ans)