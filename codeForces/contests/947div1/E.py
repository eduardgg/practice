
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, q = line()
    c = line()
    black = {i+1 for i in range(n) if c[i]}
    t = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x, y = line()
        t[x].append(y)
        t[y].append(x)
    
    bc = [0 for _ in range(n+1)]
    pare = [0 for _ in range(n+1)]
    stack = [1]
    while stack:
        v = stack.pop()
        if v in black: bc[pare[v]] += 1
        for e in t[v]:
            if e != pare[v]:
                pare[e] = v
                stack.append(e)
    
    dobles = set()
    nums1 = 0
    for i in range(n+1):
        if bc[i] == 2: dobles.add(i)
        elif bc[i] == 1: nums1 += 1

    paresb = len({e for e in black if pare[e] in black})

    for _ in range(q):
        u = int(input())
        if u in black:
            paresb -= bc[u] + (pare[u] in black)
            black.remove(u)
            if bc[pare[u]] == 1: nums1 -= 1
            elif bc[pare[u]] == 2: dobles.remove(pare[u])
            bc[pare[u]] -= 1
            if bc[pare[u]] == 2: dobles.add(pare[u])
            elif bc[pare[u]] == 1: nums1 += 1
        else:
            black.add(u)
            paresb += bc[u] + (pare[u] in black)
            if bc[pare[u]] == 1: nums1 -= 1
            elif bc[pare[u]] == 2: dobles.remove(pare[u])
            bc[pare[u]] += 1
            if bc[pare[u]] == 2: dobles.add(pare[u])
            elif bc[pare[u]] == 1: nums1 += 1

        if len(dobles) == 1 and nums1 + 2 == len(black) and paresb == len(black)-1 and pare[list(dobles)[0]] not in black:
            print("Yes")
        elif not dobles and nums1 == len(black) and paresb == len(black)-1:
            print("Yes")
        else:
            print("No")