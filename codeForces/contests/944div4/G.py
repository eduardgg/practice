
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    m = []
    d = {}
    for e in a:
        clau = (e-(e%4))//4
        if clau in d.keys():
            m[d[clau]].append(e)
        else:
            d[clau] = len(m)
            m.append([e])
    for v in m:
        v.sort(reverse = True)
    ans = []
    for e in a:
        clau = (e-(e%4))//4
        ans.append(m[d[clau]].pop())
    print(*ans)