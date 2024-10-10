
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m, k = line()
    a = line()
    b = line()
    da, db = {}, {}
    for e in b:
        db[e] = db.get(e, 0) + 1
    for e in a[:m]:
        da[e] = da.get(e, 0) + 1

    matchs = 0
    for e in da.keys():
        matchs += min(da[e], db.get(e, 0))
    
    ans = int(matchs >= k)
    for i in range(n-m):
        da[a[i]] -= 1
        if da[a[i]] < db.get(a[i], 0):
            matchs -= 1
        da[a[m+i]] = da.get(a[m+i], 0) + 1
        if da[a[m+i]] <= db.get(a[m+i], 0):
            matchs += 1
        if matchs >= k:
            ans += 1
    
    print(ans)