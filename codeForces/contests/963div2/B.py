
t = int(input())
for tc in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pars = []
    topSen = -1
    for e in a:
        if not e%2:
            pars.append(e)
        else:
            topSen = max(topSen, e)
    if len(pars) in {0, n}:
        print(0)
        continue
    ans = 0
    pars.sort()
    ok = False
    for e in pars:
        if e < topSen:
            topSen += e
            ans += 1
        else:
            ok = True
            break
    ans = len(pars) + int(ok)
    print(ans)