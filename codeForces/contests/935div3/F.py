
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    v = line()
    p = line()
    m = [(v[i], i+1) for i in range(n)]
    m.sort()
    m = m[::-1]

    top = m[0][0]
    maxStr = m[0][0]
    minMsh = 1
    forb = set()
    cjt = {m[0][1]}
    i = 2
    j = 0

    while i <= n:
        forb.add(p[i-2])
        if p[i-2] in cjt:
            cjt.remove(p[i-2])
        while len(cjt) < i:
            j += 1
            if j >= n:
                break
            if m[j][1] not in forb:
                cjt.add(m[j][1])
        if j >= n:
            break
        if m[j][0] * i > top:
            top = m[j][0] * i
            maxStr = m[j][0]
            minMsh = i
        i += 1
    
    print(top, minMsh)