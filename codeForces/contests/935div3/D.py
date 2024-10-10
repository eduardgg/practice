
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m = line()
    a = line()
    b = line()

    cur = a[m-1]
    ans = cur
    for i in range(m-2, -1, -1):
        cur += (a[i] - a[i+1] + b[i+1])
        ans = min(ans, cur)
    for i in range(m, n):
        ans += min(a[i], b[i])
    
    print(ans)