
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, x, y = line()
    a = line()
    a.sort()

    par = []
    sen = []

    for i in range(x-1):
        dif = a[i+1]-a[i]
        if dif%2:
            sen.append(dif)
        else:
            par.append(dif)
    dif = a[0] + (n-a[-1])
    if dif%2:
        sen.append(dif)
    else:
        par.append(dif)

    par.sort()
    yini = y
    ext = 0
    i = 0
    while y >= 0 and i < len(par):
        talls = par[i]//2 - 1
        if y >= talls:
            ext += talls + 1
            y -= talls
        else:
            ext += y
            y = 0
        i += 1
    
    i = 0
    while y > 0 and i < len(sen):
        talls = min(sen[i]//2, y)
        ext += talls
        y -= talls
        i += 1

    ints = x + (yini - y) - 2
    ans = ext + ints
    print(ans)