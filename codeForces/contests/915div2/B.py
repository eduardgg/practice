
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    deg = [0]*(n+1)
    for _ in range(n-1):
        u, v = line()
        deg[u] += 1
        deg[v] += 1
    fulles = 0
    for i in range(n+1):
        if deg[i] == 1:
            fulles += 1
    ans = (fulles + 1)//2
    print(ans)