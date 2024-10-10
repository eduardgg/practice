
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    v = [False]*(n+2)
    v[a[0]] = True
    ok = True
    for e in a[1:]:
        if v[e-1] or v[e+1]:
            v[e] = True
            continue
        else:
            ok = False
            break
    print("YES" if ok else "NO")