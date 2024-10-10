
for _ in range(int(input())):
    n, s, m = list(map(int, input().split()))
    v = []
    for _ in range(n):
        l, r = list(map(int, input().split()))
        v.append((l, r))
    v.sort()
    v.append((m, m))
    prevl = 0
    ok = False
    for (l, r) in v:
        if l-prevl >= s:
            ok = True
            break
        prevl = r
    print("YES" if ok else "NO")