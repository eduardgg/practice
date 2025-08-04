
for _ in range(int(input())):
    n = int(input())
    p = [0] + list(map(int, input().split()))
    swaps = 0
    pos = [-1]*(n+1)
    for i in range(1, n+1):
        pos[p[i]] = i
    for i in range(1, n+1):
        if p[i] == i:
            continue
        if p[p[i]] == i:
            continue
        swaps += 1
        aux, posi = p[p[i]], pos[i]
        p[p[i]], p[pos[i]] = i, p[p[i]]
        pos[i] = p[i]
        pos[aux] = posi
    print(swaps)