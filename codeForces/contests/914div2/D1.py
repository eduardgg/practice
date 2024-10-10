
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    a = line()
    b = line()
    ok = True
    v = [[] for _ in range(n+1)]
    for i in range(n):
        if a[i] > b[i]:
            ok = False
            break
        v[b[i]].append(i)
    if not ok:
        print("NO")
        continue
    for w in v:
        for i in w:
            if a[i] == b[i]:
                continue
            j = i
            oki = False
            while j > 0:
                j -= 1
                if a[j] == b[i]:
                    oki = True
                    break
                if b[j] < b[i] or a[j] > b[i]:
                    break
            if oki:
                e = a[j]
                while j < i:
                    j += 1
                    a[j] = e
            else:
                j = i
                oki = False
                while j < n-1:
                    j += 1
                    if a[j] == b[i]:
                        oki = True
                        break
                    if b[j] < b[i] or a[j] > b[i]:
                        break
                if oki:
                    e = a[j]
                    while j > i:
                        j -= 1
                        a[j] = e
                else:
                    ok = False
                    break
        if not ok:
            break
    if ok:
        print("YES")
    else:
        print("NO")