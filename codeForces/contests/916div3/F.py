
line = lambda : list(map(int, input().split()))
t = int(input())

for _ in range(t):
    n = int(input())
    p = line()
    parent = [None]*(n+1)
    child = [[] for _ in range(n+1)]
    for i in range(n-1):
        parent[i+2] = p[i]
        child[p[i]].append(i+2)
    bfs = []
    v = [1]
    while v:
        newv = []
        for e in v:
            for c in child[e]:
                bfs.append(c)
                newv.append(c)
        v = newv
    size = [None] + [1]*n
    while bfs:
        e = bfs.pop()
        size[parent[e]] += size[e]
    
    ans = 0
    res = 0
    top = 1
    # print(size)
    while child[top]:
        s = 0
        newtop = child[top][0]
        for e in child[top]:
            s += size[e]
            if size[e] > size[newtop]:
                newtop = e
        top = newtop
        # print("top, res, s: ", top, res, s)
        if s - size[top] + res >= size[top]:
            ans += (res + s)//2
            res = 0
            break
        else:
            res += (s - size[top])
            if res:
                ans += 1 # El node actual "top"
                res -= 1
                # print("ans+1, i res-1, ara valen:", ans, res)
    
    ans += (res+1)//2
    print(ans)