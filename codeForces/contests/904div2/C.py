
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m = line()
    setpos = set()
    ints = []
    for _ in range(n):
        l, r = line()
        ints.append((l, r))
        setpos.add(l)
        setpos.add(r)
    vecpos = list(setpos)
    vecpos.sort()
    pos = {}
    for i in range(len(vecpos)):
        pos[vecpos[i]] = i
    
    # Opció 1 - Sense 1:
    incr = [0]*(len(vecpos)+1)
    for (l, r) in ints:
        if l > 1:
            incr[pos[l]] += 1
            incr[pos[r]+1] -= 1
    acum = [0]
    maxim1 = 0
    for i in incr:
        acum.append(acum[-1]+i)
        if acum[-1] > maxim1:
            maxim1 = acum[-1]

    # Opció 2 - Sense m:
    incr = [0]*(len(vecpos)+1)
    for (l, r) in ints:
        if r < m:
            incr[pos[l]] += 1
            incr[pos[r]+1] -= 1
    acum = [0]
    maxim2 = 0
    for i in incr:
        acum.append(acum[-1]+i)
        if acum[-1] > maxim2:
            maxim2 = acum[-1]

    maxim = max(maxim1, maxim2)
    print(maxim)