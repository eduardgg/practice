
for _ in range(int(input())):
    n = int(input())
    s = input()
    cjt = list(set(e for e in s))
    cjt.sort()
    d = {}
    for i in range(len(cjt)):
        d[cjt[i]] = i
    r = []
    for e in s:
        r.append(cjt[-1-d[e]])
    ans = ''.join(r)
    print(ans)