
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = [-1]*n
    d = {}
    for i in range(n):
        if a[i] not in d.keys():
            d[a[i]] = i
        b[i] = d[a[i]]

    m = int(input())
    for _ in range(m):
        s = input()
        if len(s) != n:
            print("NO")
            continue
        
        ds = {}
        ok = True
        for i in range(n):
            if s[i] not in ds.keys():
                ds[s[i]] = i
            if b[i] != ds[s[i]]:
                ok = False
                break

        print("YES" if ok else "NO")