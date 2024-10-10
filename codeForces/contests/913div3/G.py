
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    s = input()
    encesos = {i+1 for i in range(n) if s[i] == '1'}
    a = [0] + line()
    if len(encesos) % 2:
        print(-1)
        continue
    switches = set()
    indeg = [0]*(n+1)
    for i in range(1, n+1):
        indeg[a[i]] += 1
    leaves = [e for e in range(1, n+1) if indeg[e] == 0]
    while leaves:
        l = leaves.pop()
        if l in encesos:
            switches.add(l)
            encesos.remove(l)
            # encesos.symmetric_difference_update({a[l]})
            if a[l] in encesos:
                encesos.remove(a[l])
            else:
                encesos.add(a[l])
        indeg[a[l]] -= 1
        if indeg[a[l]] == 0:
            leaves.append(a[l])
    # Ara només queden cicles, els analitzem per separat.
    # De fet, aquí leaves haurien de ser tots els nodes restants.
    ok = True
    while encesos:
        e = encesos.pop()
        sw = [{e}, set()]
        enc = 0
        ini = e
        while a[e] != ini:
            e = a[e]
            if e in encesos:
                encesos.remove(e)
                enc = 1-enc
            sw[enc].add(e)
        if enc == 0:
            ok = False
            break
        if len(sw[0]) <= len(sw[1]):
            switches = switches.union(sw[0])
        else:
            switches = switches.union(sw[1])
    if not ok:
        print(-1)
    else:
        print(len(switches))
        print(*switches)