
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
    
    dp = [[-1 for _ in range(n)] for _ in range(20)]
    for u in dfs[::-1]:
        for i in range(20):
            dp[i][u] = i*a[u] + sum([min([dp[j][v] for j in range(20) if j != i]) for v in t[u] if v != parent[u]])

    ans = sum(a) + min([dp[i][0] for i in range(20)])
    print(ans)