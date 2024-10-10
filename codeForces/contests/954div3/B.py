
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            v = []
            if i > 0: v.append(a[i-1][j])
            if i < n-1: v.append(a[i+1][j])
            if j > 0: v.append(a[i][j-1])
            if j < m-1: v.append(a[i][j+1])
            a[i][j] = min(a[i][j], max(v))
        print(*a[i])