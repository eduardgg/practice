
import bisect
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m, k = line()
    a = line()
    s = set(line())
    d = [e for e in s]
    s = set(line())
    f = [e for e in s]
    m, k = len(d), len(f)
    d.sort()
    f.sort()
    
    dif1, dif2 = a[1]-a[0], 0
    l, r = a[0], a[1]
    for i in range(1, n-1):
        if a[i+1]-a[i] >= dif1:
            dif1, dif2 = a[i+1]-a[i], dif1
            l, r = a[i], a[i+1]
        elif a[i+1]-a[i] > dif2:
            dif2 = a[i+1]-a[i]
        
    top = dif1
    fet = False
    for i in range(m):
        # bisect_left(v, k) = primer i tal que v[i] >= k
        j1 = bisect.bisect_left(f, r-top-d[i])
        j2 = bisect.bisect_left(f, l+top-d[i])
        for j in range(j1, j2):
            val = d[i]+f[j]
            top = min(top, max(r-val, val-l))
            if top == (dif1+1)//2 or (top <= dif2):
                fet = True
                break
        if fet:
            break
    
    print(max(top, dif2))