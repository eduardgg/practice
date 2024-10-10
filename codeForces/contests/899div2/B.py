
t = int(input())
for _ in range(t):
    n = int(input())
    M = []
    for i in range(n):
        M += [list(map(int, input().split()))]
        M[i].pop(0)
    

    u = set()
    for v in M:
        for x in v:
            u.add(x)

    ans = 0
    for r in u:
        u2 = set()
        for v in M:
            contains = False
            for x in v:
                if x == r:
                    contains = True
            if not contains:
                for x in v:
                    u2.add(x)
        ans = max(ans, len(u2))

    print(ans)