
line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    s = "X" + input()
    T = [[] for _ in range(n+1)]
    d = [0]*(n+1)
    status = [c for c in s]
    walls = 0

    for i in range(n-1):
        T[a[i]].append(i+2)
        T[i+2].append(a[i])
        d[a[i]] += 1
        d[i+2] += 1

    leaves = []
    for i in range(1, n+1):
        if d[i] == 1:
            leaves.append(i)
    
    dps = [0]*(n+1)
    dpp = [0]*(n+1)
    while leaves:
        leaf = leaves.pop()
        d[leaf] -= 1
        for w in T[leaf]:
            if d[w] == 0:
                continue
            
            if status[w] == 'C':
                if status[leaf] == 'P':
                    dps[w] += (1 + dpp[leaf])
                    dpp[w] += dpp[leaf]
                elif status[leaf] == 'S':
                    dps[w] += dps[leaf]
                    dpp[w] += (1 + dps[leaf])
                else:
                    dps[w] += min(dps[leaf], dpp[leaf] + 1)
                    dpp[w] += min(dpp[leaf], dps[leaf] + 1)
            elif status[w] == 'P':
                if status[leaf] == 'P':
                    dpp[w] += dpp[leaf]
                elif status[leaf] == 'S':
                    dpp[w] += (1 + dps[leaf])
                else:
                    dpp[w] += min(dpp[leaf], 1 + dps[leaf])
            else:
                if status[leaf] == 'P':
                    dps[w] += (1 + dpp[leaf])
                elif status[leaf] == 'S':
                    dps[w] += dps[leaf]
                else:
                    dps[w] += min(dps[leaf], 1 + dpp[leaf])

            d[w] -= 1
            if d[w] == 1 and w != 1:
                leaves.append(w)


    if status[1] == 'P':
        print(dpp[1])
    elif status[1] == 'S':
        print(dps[1])
    else:
        print(min(dpp[1], dps[1]))