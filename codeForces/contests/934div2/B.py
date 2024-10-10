
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    a = line()
    
    uncop = set()
    doscops = set()
    for e in a[:n]:
        if e in uncop:
            uncop.remove(e)
            doscops.add(e)
        else:
            uncop.add(e)
    l = []
    while doscops and len(l) <= 2*k-2:
        x = doscops.pop()
        l.append(x)
        l.append(x)
    
    uncop = set()
    doscops = set()
    for e in a[n:]:
        if e in uncop:
            uncop.remove(e)
            doscops.add(e)
        else:
            uncop.add(e)
    r = []
    while doscops and len(r) <= 2*k-2:
        x = doscops.pop()
        r.append(x)
        r.append(x)
    while len(r) < 2*k:
        x = uncop.pop()
        l.append(x)
        r.append(x)
    
    print(*l)
    print(*r)